from menu_item import MenuItem
import psycopg2

connection = psycopg2.connect(
    database="W4D4", 
    user='postgres',
    password='Schroon3#',
    host='localhost', #or IP address
    port='5432'
)

cursor = connection.cursor()

class MenuManager(MenuItem) :
        
    def get_by_name(name):
        query = f"SELECT * FROM menu_items WHERE item_name = '{name}'" 
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result)>0:
            item_id, item_name, item_price = result[0]
            menu_item = MenuItem(item_name, item_price)
            menu_item.item_id = item_id
            return menu_item.name
        else:
            return None
        
    def all_items() :
        query = f"SELECT * FROM menu_items"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

item2 = MenuManager.get_by_name('Beef stew')
print(item2)
items = MenuManager.all_items()
print(items)

cursor.close()
connection.close()