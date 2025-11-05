

class Order:
    def __init__(self,items ,total_price):
        self.items=items
        self.total_price=total_price

    def print_invoice(self):
        print(f"items{self.items}total_price{self.total_price}")


class Printed:
    def __init__(self,order:Order):
        print(f"items{order.items}total_price{order.total_price}")


