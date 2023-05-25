from menu_item import *

connection = psycopg2.connect(
    database="W4D4", 
    user='postgres',
    password='Schroon3#',
    host='localhost', #or IP address
    port='5432'
)

cursor = connection.cursor()

class MenuManager() :
    
    @classmethod    
    def get_by_name(cls, name) :
        query = f"SELECT * FROM menu_items WHERE item_name = '{name}'" 
        cursor.execute(query)
        result = cursor.fetchall()
        if result :
            return result
        else:
            return None
    
    @classmethod
    def all_items(cls) :
        query = f"SELECT * FROM menu_items"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

item2 = MenuManager.get_by_name('Beef stew')
print(item2)
items = MenuManager.all_items()
print(items)

