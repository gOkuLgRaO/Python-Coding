from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import os
import threading
import multiprocessing

"""
Flask: The main class for creating a Flask web application.
request: To access incoming request data.
jsonify: To convert Python dictionaries to JSON responses.
SQLAlchemy: An ORM (Object Relational Mapper) for interacting with the database.
Marshmallow: A library to handle object serialization/deserialization.
JWTManager, create_access_token, jwt_required: Utilities from flask_jwt_extended 
to handle JSON Web Tokens for authentication.
os: To access environment variables.
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'supersecretkey')
app.config['CACHE_TYPE'] = 'simple'

"""
Creates a Flask app instance.
Configures the app to use a SQLite database named app.db.
Disables modification tracking (to save resources).
Sets the JWT secret key, either from an environment variable or a default value.
"""
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
cache = Cache(app)
limiter = Limiter(get_remote_address, app=app)

"""
Initializes the SQLAlchemy instance for ORM.
Initializes Marshmallow for object serialization.
Initializes JWTManager for handling JWT authentication.
"""


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='User')  # User roles: Admin, User


"""
Defines a User model with columns for id, username, and password.
id is the primary key.
username is unique and cannot be null.
password cannot be null.
"""


# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)


"""
Defines a Resource model with columns for id and name.
id is the primary key.
name is unique and cannot be null.
"""


# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


"""
Defines a schema for serializing and deserializing User instances.
"""


# Define the Resource schema
class ResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Resource
        load_instance = True


"""
Defines a schema for serializing and deserializing Resource instances.
"""
user_schema = UserSchema()
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

"""
Creates instances of the schemas.
resources_schema is configured to handle multiple Resource instances.
"""


@app.before_request
def create_tables():
    db.create_all()


"""
Ensures the database tables are created before handling any request.
"""


# Error handling
@app.errorhandler(404)
def not_found():
    return jsonify({"error": "Resource not found"}), 404


"""
Handles 404 errors by returning a JSON response with a 404 status code.
"""


@app.errorhandler(400)
def bad_request():
    return jsonify({"error": "Bad request"}), 400


"""
Handles 400 errors by returning a JSON response with a 400 status code.
"""


# Background task example (e.g., sending email)
def background_task(email, message):
    # simulate sending an email
    logging.info(f"Sending email to {email}: {message}")


@app.route('/send-email', methods=['POST'])
@jwt_required()
def send_email():
    data = request.json
    email = data.get('email')
    message = data.get('message')
    threading.Thread(target=background_task, args=(email, message)).start()
    return jsonify({"message": "Email is being sent"}), 202


# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'User')
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201


"""
Handles user registration.
Checks if the username already exists.
If not, creates a new user and saves it to the database.
Returns the created user in JSON format.
"""


# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify(access_token=access_token)


"""
Handles user login.
Verifies the provided credentials.
If valid, generates an access token and returns it.
"""


# Create a new resource
@app.route('/resource', methods=['POST'])
@jwt_required()
@limiter.limit("10 per minute")
def create_resource():
    identity = get_jwt_identity()
    if identity['role'] != 'Admin':
        return jsonify({"error": "Permission denied"}), 403
    data = request.json
    name = data.get('name')
    if Resource.query.filter_by(name=name).first():
        return jsonify({"error": "Resource already exists"}), 400
    new_resource = Resource(name=name)
    db.session.add(new_resource)
    db.session.commit()
    return jsonify(resource_schema.dump(new_resource)), 201


"""
Creates a new resource.
Requires JWT authentication.
Checks if the resource already exists.
If not, creates and saves the new resource.
Returns the created resource in JSON format.
"""


# Read a resource
@app.route('/resource/<int:resource_id>', methods=['GET'])
@jwt_required()
def read_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return jsonify(resource_schema.dump(resource))


"""
Retrieves a specific resource by its ID.
Requires JWT authentication.
If found, returns the resource in JSON format.
"""


# Update a resource
@app.route('/resource/<int:resource_id>', methods=['PUT'])
@jwt_required()
def update_resource(resource_id):
    identity = get_jwt_identity()
    if identity['role'] != 'Admin':
        return jsonify({"error": "Permission denied"}), 403
    resource = Resource.query.get_or_404(resource_id)
    data = request.json
    resource.name = data.get('name')
    db.session.commit()
    return jsonify(resource_schema.dump(resource))


"""
Updates a specific resource by its ID.
Requires JWT authentication.
Updates the resource's name.
Saves the changes and returns the updated resource in JSON format.
"""


# Delete a resource
@app.route('/resource/<int:resource_id>', methods=['DELETE'])
@jwt_required()
def delete_resource(resource_id):
    identity = get_jwt_identity()
    if identity['role'] != 'Admin':
        return jsonify({"error": "Permission denied"}), 403
    resource = Resource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify({"message": "Resource deleted successfully"}), 200


"""
Deletes a specific resource by its ID.
Requires JWT authentication.
If found, deletes the resource and returns a success message.
"""


# List resources with pagination
@app.route('/resources', methods=['GET'])
@jwt_required()
@cache.cached(timeout=60)
def list_resources():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    resources = Resource.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        "total": resources.total,
        "pages": resources.pages,
        "current_page": resources.page,
        "resources": resources_schema.dump(resources.items)
    })


# Search and filter resources
@app.route('/resources/search', methods=['GET'])
@jwt_required()
def search_resources():
    query = request.args.get('query', '', type=str)
    resources = Resource.query.filter(Resource.name.contains(query)).all()
    return jsonify(resources_schema.dump(resources))


if __name__ == "__main__":
    app.run(debug=True)

"""
Runs the Flask application in debug mode.
"""
