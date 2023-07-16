"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, int(self.item_quantity), int(self.item_price), int(self.item_price * self.item_quantity)))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))



class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []


    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found_item = False
        for item in self.cart_items:
            if item.item_name == item_name:
                print()
                self.cart_items.remove(item)
                found_item = True
                break

        if not found_item:
            print("Item not found in cart. Nothing removed.\n")

    def modify_item(self, item):
        found_item = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                self.cart_items[i].item_quantity = item.item_quantity
                found_item = True
                break

        if not found_item:
            print("Item not found in cart. Nothing modified.\n")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: 0\n")
            print("SHOPPING CART IS EMPTY")
            print("\nTotal: $0\n")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}\n".format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()
            print("\nTotal: ${}\n".format(int(self.get_cost_of_cart())))


    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("\nItem Descriptions")
            for item in self.cart_items:
                item.print_item_description()
        print()


def print_menu(cart):
    menu_options = ['a', 'r', 'c', 'i', 'o', 'q']
    choice = ''
    while True:
        if choice in menu_options or choice == '':
            print("MENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")

        choice = input("\nChoose an option:")

        if choice not in menu_options:
            continue

        if choice == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)

        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(item_name, 0, new_quantity)
            cart.modify_item(item)

        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            print()
            break

try:
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print("\nCustomer name: {}".format(customer_name))
    print("Today's date: {}\n".format(current_date))

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)
except:
    print()



