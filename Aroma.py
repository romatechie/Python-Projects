menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Maggie': 70,
    'Salad': 80,
}
comment_art = """
             _____  ____   __  __           ____  ______    ____ _____ _   _          _____ 
       /\   |  __ \/ __ \ |  \/  |   /\    / __ \|  ____|  |  _ \_  __| | |  |  /\   |  __ \ 
      /  \  | |__) | |  | | \  / |  /  \   | |  | | |__    | |_) || | | |__| | /  \  | |__) |
     / /\ \ |  _  /| |  | | |\/| | / /\ \  | |  | |  __|   |  _ < | | |  __  |/ /\ \ |  _  / 
    / ____ \| | \ \| |__| | |  | |/ ____ \ | |__| | |      | |_) || |_| |  | |/ ____ \| | \ \ 
   /_/    \_\_|  \_\____/|_|  |_/_/     \_\ \____/|_|      |____/_____|_|  |_/_/    \_\_|  \_\
"""

print(comment_art)
print("\n")

print("------------------------------ Welcome to Aroma of Bihar -----------------------------")
print("--------------------------------------------------------------------------------------")
print("\n--------------------------------- Here is our Menu: --------------------------------")


for item, price in menu.items():
    print(f"{item}: Rs{price}")

menu = {key.lower(): value for key, value in menu.items()}

order_total = 0
bill = []   # to store each order detail

  # normalize keys to lowercase
while True:
    item = input("\nEnter the name of the item you want to order: ")
    item = item.lower()
    if item in menu:
        quantity = int(input(f"How many {item}s do you want? "))
        price = menu[item] * quantity
        order_total += price
        bill.append((item, quantity, menu[item], price))  # store (item, qty, unit_price, subtotal)
        print(f"{quantity} {item}(s) added to your order. Subtotal: Rs{price}")
    else:
        print(f"Sorry, {item} is not available.")

    another_order = input("Do you want to order another item? (Yes/No): ")
    if another_order.lower() != "yes":
        break

# Print final receipt
print("\n===================== BILL RECEIPT =====================")
print("{:<10} {:<10} {:<12} {:<10}".format("Item", "Qty", "Unit Price", "Total"))
print("-" * 45)

for item, qty, unit_price, subtotal in bill:
    print("{:<10} {:<10} {:<12} {:<10}".format(item, qty, unit_price, subtotal))

print("-" * 45)
print(f"Grand Total: Rs{order_total}")
print("==============================================================")
print("Thank you for visiting Aroma of Bihar!")