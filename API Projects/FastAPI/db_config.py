from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#   1. Create db address variable with the database connection
#   2. Create engine variable to bridge code with database
#   3. Create a session to manage transactions between database
db_url = "postgresql://(postgres_username):(postgres_password)@localhost:5432/products"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)