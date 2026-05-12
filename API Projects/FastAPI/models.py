from pydantic import BaseModel

#   Define the model for validation
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int