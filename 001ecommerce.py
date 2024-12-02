class User:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self, items, tax_rate, discount):
        self.items = items
        self.tax_rate = tax_rate
        self.discount = discount

    def calculate_total(self):
        subtotal = sum(self.items)
        tax = subtotal * self.tax_rate
        discount_amount = subtotal * self.discount
        return subtotal + tax - discount_amount


user = User("Rodrygo")
order1 = Order([100, 200, 300], 0.1, 0.05)
order2 = Order([50, 150], 0.1, 0.1)

user.place_order(order1)
user.place_order(order2)

print(order1.calculate_total())
print(order2.calculate_total())
