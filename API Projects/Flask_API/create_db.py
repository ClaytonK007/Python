from api import app, db

#   Create the database for requests
with app.app_context():
    db.create_all()