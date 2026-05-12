from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from db_config import session, engine
import db_models
from sqlalchemy.orm import Session

#   1. Create instance to initialize Fast API.
#   2. Configure backend to communicate with frontend.
#   3. Generate tables in database that is declared in db_models(declared base).
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)
db_models.Base.metadata.create_all(bind=engine)

#   Initial data to test API before sent to database
products = [
    Product(id=1, name="phone", description="smart phone", price=699.99, quantity=50),
    Product(id=2, name="laptop", description="gaming laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="blue ball-point", price=1.99, quantity=100),
    Product(id=4, name="Table", description="wooden table", price=199.99, quantity=20),
]

#   Initialize database connection from db_config to handle requests.
#   Prevent memory leaks by opening connection, doing operations and
#   then closing the connection.
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

#   Commit inital data to created database
def init_db():
    db = session()
    count = db.query(db_models.Product).count
    if count == 0:
        for product in products:
            db.add(db_models.Product(**product.model_dump()))
        db.commit()

init_db()

#   Create CRUD operations to manage data between app and database.
#   READ API endpoint - get/fetch all products in database
@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products

#   GET API endpoint - get/fetch all products by ID in database
@app.get("/product/{id}")
def get_product_by_id(id:int, db:Session = Depends(get_db)):
    db_products = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_products:
            return db_products
    return "product not found"

#   ADD API endpoint - add a product to database
@app.post("/products")
def add_product(product: Product, db:Session = Depends(get_db)):
    db.add(db_models.Product(**product.model_dump()))
    db.commit()
    return (product, "Product added succesfully.")

#   UPDATE API endpoint - update a product in database
@app.put("/products/{id}")
def update_product(id: int, product: Product,  db:Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated succesfully."
    else:
        return "Product not found. Cannot be updated."

#   DELETE API endpoint - delete a product in database
@app.delete("/products/{id}")
def delete_product(id: int, db:Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted successfully."
    else:
        return "Product cannot be deleted."
