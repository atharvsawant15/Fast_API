from fastapi import FastAPI
from models import Product

# FastAPI app
app = FastAPI()

# Home page normal back
@app.get("/")
def home():
    return "Home page"

# products = ["appel","banana","fish"]

products = [
    Product(id=1, name="laptop", description="gaming laptop", price=100.0, quantity=1),
    Product(id=2, name="mobile", description="oppo", price=1000.0, quantity=1),
    Product(id=3, name="tablet", description="android tablet", price=500.0, quantity=2),
    Product(id=4, name="headphones", description="wireless headphones", price=150.0, quantity=3),
    Product(id=5, name="keyboard", description="mechanical keyboard", price=120.0, quantity=4)
Product(id=6, name="key", description="mechanical keyboard", price=130.0, quantity=6)
]

@app.get("/products/{id}")
def specific_product(id: int):
    for product in products:
        if product.id == id:
            return products[id-1]
    return "product not found"

@app.get("/products")
def get_all_products():
    return products

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated succefully"
    return "product not found" 

@app.delete("/products")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "deleted sucessfully"
    return "product not found"       
