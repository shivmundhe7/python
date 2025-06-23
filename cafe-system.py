# Menu Of the restaurant
menu = {
    'pizza': 70,
    'pasta': 80,
    'salad': 40,
    'coffee': 50,
    'bun paav': 30,
}

# Greet
print('Welcome To Python Restaurant')
print("Pizza : Rs 70\nPasta : Rs 80\nSalad : Rs 40\nCoffee : Rs 50\nBun Paav : Rs 30")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1.title()}' has been added to your order.")
else:
    print(f"Sorry, item '{item_1}' is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2.title()}' has been added to order.")
    else:
        print(f"Sorry, item '{item_2}' is not available!")

print(f"Total amount to pay is Rs {order_total}")