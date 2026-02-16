# Simulate shopping cart: list of dicts {item: price}; loop to apply 10% discount if total >100.

# Shopping cart: list of dictionaries
cart = [
    {"item": "Laptop Bag", "price": 45},
    {"item": "Mouse", "price": 25},
    {"item": "Keyboard", "price": 50},
    {"item": "Headphone", "price": 10}
]

total = 0

# Loop to calculate total
for product in cart:
    total += product["price"]

print("Total before discount:", total)

# Apply 10% discount if total > 100
if total > 100:
    discount = total * 0.10
    total -= discount
    print("Discount applied:", discount)
else:
    print("No discount applied")

print("Final total:", total)
