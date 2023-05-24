import psycopg2
from menu_item import MenuItem
from menu_manager import MenuManager

connection = psycopg2.connect(
    database="W4D4", 
    user='postgres',
    password='Schroon3#',
    host='localhost', #or IP address
    port='5432'
)

cursor = connection.cursor()

def show_user_menu() :
    user_input = input('Program menu:\nView an Item (V)\nAdd an Item (A)\nDelete an Item (D)\nUpdate an Item (U)\nShow the Menu (S) \nChose an action: ')
    try :
        if user_input.lower == 'v' :
            user_item = input('Enter an item name: ')
            user_menu_item = MenuManager.get_by_name(user_item)
            if user_menu_item :
                print(f'Item: {user_menu_item.name}, Price: {user_menu_item.price}')
            else :
                print('Item not found')
        elif user_input.lower == 'a' :
            item_name = input("Enter the item name to add: ")
            item_price = float(input("Enter the item price: "))
            menu_item = MenuItem(item_name, item_price)
            menu_item.save()
            print("Item added successfully.")
        elif user_input.lower == 'd' :
            item_to_delete = int(input("Enter the item name to delete: "))
            name_to_delete = MenuManager.get_by_name(item_to_delete)
            if name_to_delete:
                MenuItem.delete(name_to_delete)
                print("Item deleted successfully.")
            else:
                print("Item not found.")
        elif user_input.lower == "u":
            item_name = int(input("Enter the item name to update: "))
            menu_item = MenuManager.get_by_name(item_name)
            if menu_item:
                new_name = input("Enter the new name: ")
                new_price = float(input("Enter the new price (leave empty to keep current price): "))
                menu_item.update(new_name, new_price)
                print("Item updated successfully.")
            else:
                print("Item not found.")
        elif user_input.lower == 's' :
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
    except :
        print("Invalid choice. Please try again.")
        
show_user_menu()

cursor.close()
connection.close()