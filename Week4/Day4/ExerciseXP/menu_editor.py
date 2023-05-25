import psycopg2
from menu_item import *
from menu_manager import *

def show_user_menu() :
    user_input = input('Program menu:\nView an Item (V)\nAdd an Item (A)\nDelete an Item (D)\nUpdate an Item (U)\nShow the Menu (S) \nChose an action: ').lower()
    if user_input == 'v' :
        view_item_menu()
    if user_input == 'a' :
        add_item_to_menu()
    elif user_input == 'd' :
        remove_item_from_menu()
    elif user_input == "u" :
        update_item_from_menu()
    elif user_input == 's' :
        show_retaurant_menu()
    else :
        print("Invalid choice. Please try again.")

def view_item_menu() :
            user_item = input('Enter an item name to view: ')
            user_menu_item = MenuManager.get_by_name(user_item)
            if user_menu_item :
                print(f'Item: {user_menu_item}')
            else :
                print('Item not found')
                
def add_item_to_menu():
            item_name = str(input("Enter the item name to add: "))
            item_price = float(input("Enter the item price: "))
            menu_item = MenuItem(item_name, item_price)
            menu_item.save()
            print("Item added successfully.")
    
def remove_item_from_menu() :
            item_to_delete = (input("Enter the item name to delete: "))
            name_to_delete = MenuManager.get_by_name(item_to_delete)
            if name_to_delete:
                item = MenuItem(item_to_delete)
                item.delete()
                print("Item deleted successfully.")
            else:
                print("Item not found.")
        
def update_item_from_menu() :
        item_name = (input("Enter the item name to update: "))
        menu_item = MenuManager.get_by_name(item_name)
        if menu_item:
                new_name = input("Enter the new name: ")
                new_price = float(input("Enter the new price (leave empty to keep current price): "))
                item = MenuItem(item_name)
                item.update(new_name, new_price)
                print("Item updated successfully.")
        else:
                print("Item not found.")

def show_retaurant_menu() :
            full_menu_items = MenuManager.all_items()
            if full_menu_items:
                print("Menu Items:")
                for item_id, item_name, item_price in full_menu_items:
                    print(f"Item ID: {item_id}")
                    print(f"Item: {item_name}")
                    print(f"Price: {item_price}")
                    print("---------------------")
                else:
                    print("No items found in the menu.")


        
        

show_user_menu()

