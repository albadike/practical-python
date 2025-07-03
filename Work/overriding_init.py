class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        print("I can see you called the Parent's cost()")
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Calling the parent's __init__ method with super()
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        # Overriding the parent's cost() as well
        return self.factor * super().cost()
    
    
# Example usage
my_stock = MyStock('NVDA', 100, 4003.45, 1.25)
print(my_stock.cost())  
print(isinstance(my_stock, Stock))  