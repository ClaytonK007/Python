from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

#   1. Create instance to initialize web app.
#   2. Create configuration line to use SQLite database stored  
#      in a file called database.db.
#   3. Initialize flask-sqlalchemy and connect to flask app to 
#      the database.
#   4. Define api with flask_restful
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)
api = Api(app)

#   Model ORM data
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    #   Bridge between the Object and the database
    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"

#   Define arguments to send data to API and set validation
user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, required=True, help="Name cannot be blank.")
user_args.add_argument("email", type=str, required=True, help="Email cannot be blank.")

#   Definitions for user fields
userFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String
}

#   Object to handle API requests related to data - Retrieve users from db
#   Return Json in serialized format with decorator
#   Add POST request to retrieve data
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
#   CRUD method for User
#   Return Json in serialized format with decorator
class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user
    
    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user
    
    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

#   Register Users and User class as an API endpoint
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

#   Create routes/endpoints where data is requested from browser
@app.route('/')
def home():
    return "<h1>Flask REST API</h1>"

#   Get server to run when file is execued
if __name__ == "__main__":
    app.run(debug=True)