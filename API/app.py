from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, fields, validate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import os
from celery import Celery

"""
RotatingFileHandler: Manages the logging files and rotates them when they reach a certain size
Flask: the Flask class to create the application
request, jsonify, abort: functions provided by flask to handle requests, return JSON responses, and abort requests
SQLAlchemy: an ORM that helps interact with database
Marshmallow: library for object serialization and deserialization
flask_marshmallow: integrates flask and marshmallow
ValidationError, fields, validate: used for data validation in marshmallow
JWTManager, create_access_token, jwt_required, get_jwt_identity: Flask-JWT-Extended functions for handling 
JSON Web Tokens (JWT) for authentication.
Cache: extension for caching
Limiter, get_remote_address: flask limiter for rate limiting API calls
Migrate: flask migrate helps manage database migration
wraps: A decorator from 'functools' module to preserve metadata when wrapping functions with decorators.
generate_password_hash, check_password_hash: Utilities from Werkzeug to securely hash and check passwords.
logging: Python’s built-in logging module.
os: For interacting with the operating system, such as reading environment variables.
Celery: A distributed task queue library for handling background jobs.

"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'supersecretkey')
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # Tokens expire after 1 hour
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 86400  # Refresh tokens expire after 24 hours
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

"""
app = Flask(__name__): Initializes the Flask application. __name__ helps Flask to locate resources 
(like templates and static files).
SQLALCHEMY_DATABASE_URI: Specifies the database connection URI. Here it's an SQLite database file named app.db.
SQLALCHEMY_TRACK_MODIFICATIONS: Disables a feature that signals the application every time a change 
is made to the database. It saves memory.
JWT_SECRET_KEY: Secret key used for encoding and decoding JWT tokens. It’s either fetched from an 
environment variable or defaults to 'supersecretkey'.
CACHE_TYPE: Defines the caching backend. Here, it's Redis.
CACHE_REDIS_URL: URL for connecting to the Redis server for caching.
JWT_ACCESS_TOKEN_EXPIRES: Sets the expiration time for access tokens (1 hour).
JWT_REFRESH_TOKEN_EXPIRES: Sets the expiration time for refresh tokens (24 hours).
CELERY_BROKER_URL and CELERY_RESULT_BACKEND: Configures Celery to use Redis for 
message brokering and storing task results.
"""

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
cache = Cache(app)
limiter = Limiter(get_remote_address, app=app)
migrate = Migrate(app, db)
celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                broker=app.config['CELERY_BROKER_URL'])

"""
db: Initializes SQLAlchemy, which will manage database interactions.
ma: Initializes Marshmallow, which will handle serialization, deserialization, and validation of data.
jwt: Initializes JWTManager, which handles JWT-based authentication.
cache: Initializes caching with Redis as the backend.
limiter: Initializes Flask-Limiter for rate limiting API calls, using the client's IP address to identify the rate limit
migrate: Initializes Flask-Migrate for handling database migrations.
celery: Initializes Celery for handling background tasks, using Redis for message brokering and result storage.

"""

# Enhanced logging setup
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Application startup')

"""
Checks if a logs directory exists. If not, it creates one.
RotatingFileHandler: Manages logging to a file with rotation (creates a new file when the current one reaches 10MB, 
and keeps up to 10 backup files).
Formatter: Specifies the format for log messages.
file_handler.setLevel(logging.INFO): Sets the logging level to INFO, meaning it will capture all messages 
at this level and above (like WARNING, ERROR).
app.logger.addHandler(file_handler): Adds the file handler to the app's logger.
app.logger.info('Application startup'): Logs a startup message when the app begins.

"""


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='User')  # User roles: Admin, User


"""
id: Primary key, auto-incremented integer.
username: A string of up to 80 characters, must be unique and not null.
password: A string of up to 120 characters, not null, stores the hashed password.
role: A string indicating the user's role (e.g., 'Admin' or 'User'). Defaults to 'User'.
"""


# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(255), nullable=False)  # New field
    cost = db.Column(db.Float, nullable=False)  # New field


"""
id: Primary key, auto-incremented integer.
name: A string of up to 120 characters, must be unique and not null.
location: A string of up to 255 characters, not null, stores the resource's location.
cost: A float, not null, stores the resource's cost.
"""


# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


"""
Used for serializing and deserializing User objects.
load_instance = True: This option will return a model instance when deserializing data.
"""


# Define the Resource schema with validation
class ResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Resource
        load_instance = True

    name = fields.Str(required=True, validate=validate.Length(min=1))
    location = fields.Str(required=True, validate=validate.Length(min=1))
    cost = fields.Float(required=True, validate=validate.Range(min=0.01))


"""
Used for serializing and deserializing Resource objects.
name, location, cost: Fields with validation rules to ensure that the data is correct before saving it to the database.
"""
user_schema = UserSchema()
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

"""
user_schema: Instance of UserSchema, used to serialize/deserialize single user objects.
resource_schema: Instance of ResourceSchema, used to serialize/deserialize single resource objects.
resources_schema: Instance of ResourceSchema with many=True, used to serialize/deserialize lists of resource objects.
"""


@app.before_request
def create_tables():
    db.create_all()


"""
@app.before_request: This decorator registers a function that runs before each request.
db.create_all(): Ensures that all tables are created in the database before any request is processed.
"""


# Custom error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"error": e.messages}), 400


# Error handling for not found and bad request
@app.errorhandler(404)
def not_found():
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(400)
def bad_request():
    return jsonify({"error": "Bad request"}), 400


"""
ValidationError: Handles errors related to data validation failures.
404: Returns a custom JSON response if a requested resource is not found.
400: Returns a custom JSON response for bad requests.
"""


# Background task using Celery
@celery.task
def send_email_task(email, message):
    logging.info(f"Sending email to {email}: {message}")


"""
@celery.task: Registers the function as a Celery task that can run asynchronously.
send_email_task: A placeholder function that logs an email message. In a real app, this would send an email.
"""


@app.route('/send-email', methods=['POST'])
@jwt_required()
def send_email():
    data = request.json
    email = data.get('email')
    message = data.get('message')
    send_email_task.delay(email, message)
    return jsonify({"message": "Email is being sent"}), 202


"""
@app.route('/send-email', methods=['POST']): Defines a POST route for sending emails.
@jwt_required(): Requires a valid JWT token to access this route.
send_email_task.delay(email, message): Queues the email task to be processed in the background.
"""


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
@app.route('/register', methods=['POST']): Defines a POST route for user registration.
It extracts user data from the request, checks if the username already exists, hashes the password, 
and saves the new user to the database.
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
@app.route('/login', methods=['POST']): Defines a POST route for user login.
It verifies the username and password, then generates a JWT token if the credentials are valid.
"""


# Role-based access control decorator
def role_required(required_role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            identity = get_jwt_identity()
            if identity['role'] != required_role:
                abort(403, description="Permission denied")
            return fn(*args, **kwargs)

        return decorator

    return wrapper


"""
role_required(required_role): A decorator function that restricts access to certain routes based on the user’s role.
It checks the user’s role from the JWT token and aborts the request if the role doesn't match.
"""


# Create a new resource
@app.route('/resource', methods=['POST'])
@jwt_required()
@role_required('Admin')
@limiter.limit("10 per minute", key_func=lambda: get_jwt_identity()['role'])
def create_resource():
    data = request.json
    try:
        new_resource = resource_schema.load(data)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    db.session.add(new_resource)
    db.session.commit()
    return jsonify(resource_schema.dump(new_resource)), 201


"""
@app.route('/resource', methods=['POST']): Defines a POST route for creating a resource.
Requires a JWT token and an Admin role.
Rate limited to 10 requests per minute per user.
Validates and creates a new resource in the database.
"""


# Read a resource
@app.route('/resource/<int:resource_id>', methods=['GET'])
@jwt_required()
def read_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return jsonify(resource_schema.dump(resource))


"""
@app.route('/resource/<int:resource_id>', methods=['GET']): Defines a GET route for fetching a single resource by its ID
Requires a JWT token and returns the resource if found.
"""


# Update a resource
@app.route('/resource/<int:resource_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin')
def update_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    data = request.json
    try:
        updated_resource = resource_schema.load(data, instance=resource, partial=True)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    db.session.commit()
    return jsonify(resource_schema.dump(updated_resource))


"""
@app.route('/resource/<int:resource_id>', methods=['PUT']): Defines a PUT route for updating a resource.
Requires a JWT token and an Admin role.
Partially updates the resource with validated data.
"""


# Delete a resource
@app.route('/resource/<int:resource_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin')
def delete_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify({"message": "Resource deleted successfully"}), 200


"""
@app.route('/resource/<int:resource_id>', methods=['DELETE']): Defines a DELETE route for removing a resource.
Requires a JWT token and an Admin role.
Deletes the specified resource from the database.
"""


# List resources with pagination and sorting
@app.route('/resources', methods=['GET'])
@jwt_required()
@cache.cached(timeout=60, query_string=True)
def list_resources():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    sort_by = request.args.get('sort_by', 'id')
    sort_order = request.args.get('sort_order', 'asc')

    query = Resource.query

    # Apply sorting
    if sort_order == 'desc':
        query = query.order_by(db.desc(getattr(Resource, sort_by)))
    else:
        query = query.order_by(getattr(Resource, sort_by))

    resources = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "total": resources.total,
        "pages": resources.pages,
        "current_page": resources.page,
        "resources": resources_schema.dump(resources.items)
    })


"""
@app.route('/resources', methods=['GET']): Defines a GET route for listing resources with pagination and sorting.
Requires a JWT token.
Caches the results for 60 seconds.
Supports pagination (page, per_page) and sorting (sort_by, sort_order).
"""


# Search and filter resources
@app.route('/resources/search', methods=['GET'])
@jwt_required()
def search_resources():
    query = request.args.get('query', '', type=str)
    resources = Resource.query.filter(Resource.name.contains(query)).all()
    return jsonify(resources_schema.dump(resources))


"""
@app.route('/resources/search', methods=['GET']): Defines a GET route for searching resources by name.
Requires a JWT token.
Filters resources by checking if their name contains the search query.
"""


# Refresh token endpoint
@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


"""
@app.route('/refresh', methods=['POST']): Defines a POST route for refreshing JWT tokens.
Requires a valid refresh token.
Returns a new access token.
"""
if __name__ == "__main__":
    app.run(debug=True)

"""
if __name__ == "__main__":: This block ensures that the Flask app runs only if the script is executed directly.
app.run(debug=True): Starts the Flask development server in debug mode, which provides useful debugging information.
"""