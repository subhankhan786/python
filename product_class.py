from dataclasses import dataclass

@dataclass
class Product():
    name : str
    id : int
    price : float
    quantity : float
    category : str