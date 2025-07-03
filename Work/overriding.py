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
    # def cost(self):
    #     # Redefining (or Overwriting) a parent's method in the child class
    #     print("I can see you called the Child's cost()")

    def cost(self):
        # Overriding the parent's method in the child class
        actual_cost = super().cost()    # super() is the parent's self
        print(f"Actual cost from super: {actual_cost}")
        return 1.25 * actual_cost


my_stock = MyStock('ACME', 100, 123.45)
print(my_stock.cost())  # Should print 12345.0 * 1.25 = 15431.25
