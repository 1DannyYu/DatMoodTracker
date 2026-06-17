products = {
    "Milk": 1.99,
    "Oranges": 2.48,
    "Bread": 3.99,
    "Eggs": 1.99
}

item = input("Enter an item name: ")

if item in products:
    print(f"The cost of {item} is ${products[item]:.2f}.")
else:
    print("Sorry, that item is not available.")