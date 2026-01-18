from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price:float
    quantity: int

# we dont required contructor when we use Basemodel has it validates the data
    # def __init__(self,id:int,name:str,descriptiion:str,price:float,qunantity:str):
    #     self.id = id
    #     self.name = name
    #     self.description = descriptiion
    #     self.price = price
    #     self.quantity = qunantity