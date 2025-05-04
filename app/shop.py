from app.product import Product


class Shop:
    def __init__(self,
                 name: str,
                 products: Product,
                 location: list) -> None:
        self.name = name
        self.products = products
        self.location = location
