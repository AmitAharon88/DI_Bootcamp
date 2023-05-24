import psycopg2

class MenuItem :
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

    
    def save(self):
        query_user = f"""
        INSERT INTO menu_items 
        (item_name, item_price)
        VALUES ('{self.name}', {self.price})
         """
        cursor.execute(query_user)
        connection.commit()  
        
    def delete(self):
        query_user = f"""
        DELETE FROM menu_items WHERE item_name = '{self.name}'
         """
        cursor.execute(query_user)
        connection.commit() 
        
    def update(self, new_name, new_price):
        query_user = f"""
        UPDATE menu_items 
        SET item_name = '{new_name}', item_price = {new_price} WHERE item_name = '{self.name}'
         """
        cursor.execute(query_user)
        connection.commit()

connection = psycopg2.connect(
    database="W4D4", 
    user='postgres',
    password='Schroon3#',
    host='localhost', #or IP address
    port='5432'
)

cursor = connection.cursor()

item = MenuItem('Burger', 35)
item.save()
item.update('Veggie Burger', 37)
item.delete()


cursor.close()
connection.close()
