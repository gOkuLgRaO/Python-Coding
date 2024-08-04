from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'supersecretkey')

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)


# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


# Define the Resource schema
class ResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Resource
        load_instance = True


user_schema = UserSchema()
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)


@app.before_request
def create_tables():
    db.create_all()


# Error handling
@app.errorhandler(404)
def not_found():
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(400)
def bad_request():
    return jsonify({"error": "Bad request"}), 400


# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201


# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)


# Create a new resource
@app.route('/resource', methods=['POST'])
@jwt_required()
def create_resource():
    data = request.json
    name = data.get('name')
    if Resource.query.filter_by(name=name).first():
        return jsonify({"error": "Resource already exists"}), 400
    new_resource = Resource(name=name)
    db.session.add(new_resource)
    db.session.commit()
    return jsonify(resource_schema.dump(new_resource)), 201


# Read a resource
@app.route('/resource/<int:resource_id>', methods=['GET'])
@jwt_required()
def read_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return jsonify(resource_schema.dump(resource))


# Update a resource
@app.route('/resource/<int:resource_id>', methods=['PUT'])
@jwt_required()
def update_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    data = request.json
    resource.name = data.get('name')
    db.session.commit()
    return jsonify(resource_schema.dump(resource))


# Delete a resource
@app.route('/resource/<int:resource_id>', methods=['DELETE'])
@jwt_required()
def delete_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify({"message": "Resource deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
