# Inventory list: each item contains
# [item_name, category, unit_price, units_sold, units_remaining]
store_inventory = [
    ["Strawberry", "Fruit", 3.50, 40, 10],
    ["Broccoli", "Vegetable", 2.20, 25, 8],
    ["Cheddar", "Dairy", 5.00, 18, 4],
    ["Baguette", "Bakery", 2.80, 35, 2],
    ["Blueberry", "Fruit", 4.00, 22, 6],
    ["Spinach", "Vegetable", 1.80, 30, 12],
    ["Yogurt", "Dairy", 1.20, 50, 15],
    ["Croissant", "Bakery", 3.00, 28, 3],
]

# Calculate total revenue generated from all items (unit_price * units_sold)
total_revenue = 0
for index in range(len(store_inventory)):
    total_revenue += store_inventory[index][2] * store_inventory[index][3]
print("Total Revenue:", total_revenue)

# List all items with low stock (units_remaining less than 5)
for index in range(len(store_inventory)):
    if store_inventory[index][4] < 5:
        print("Low stock Item:", store_inventory[index][0])

# Calculate and print revenue category-wise for each item
for item_name, category, price_per_unit, sold_units, stock_left in store_inventory:
    item_revenue = price_per_unit * sold_units
    print(f"Category-wise Revenue for {item_name} ({category}): {item_revenue}")
