import sqlite3


db_name = "shop.db"

sql_create_categories = '''
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
'''

sql_create_stores = '''
CREATE TABLE IF NOT EXISTS stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL
)
'''

sql_create_products = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2),
    unit_price FLOAT,
    stock_quantity INTEGER,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES stores (store_id)
)
'''

def execute_query(db_name, query):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
    except sqlite3.Error as e:
        print(e)



execute_query(db_name, sql_create_categories)
execute_query(db_name, sql_create_stores)
execute_query(db_name, sql_create_products)



def insert_data(db_name, query, data):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.executemany(query, data)
            conn.commit()
    except sqlite3.Error as e:
        print(e)



categories_data = [
    ("FD", "Food products"),
    ("EL", "Electronics"),
    ("CL", "Clothes")
]

stores_data = [
    (1, "Asia"),
    (2, "Globus"),
    (3, "Spar")
]

products_data = [
    (1, "Chocolate", "FD", 10.5, 129, 1),
    (2, "Jeans", "CL", 120.0, 55, 2),
    (3, "T-Shirt", "CL", 0.0, 15, 1)
]

insert_data(db_name, "INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)", categories_data)
insert_data(db_name, "INSERT OR IGNORE INTO stores (store_id, title) VALUES (?, ?)", stores_data)
insert_data(db_name,
            "INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (?, ?, ?, ?, ?, ?)",
            products_data)



def show_stores(db_name):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stores")
        stores = cursor.fetchall()
        print("\nВы можете отобразить список продуктов по выбранному id магазина.")
        print("Введите 0 для выхода.\n")
        for store in stores:
            print(f"{store[0]}. {store[1]}")



def show_products_by_store(db_name, store_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.title, c.title, p.unit_price, p.stock_quantity
            FROM products p
            JOIN categories c ON p.category_code = c.code
            WHERE p.store_id = ?
        ''', (store_id,))
        products = cursor.fetchall()

        if not products:
            print("В этом магазине нет товаров.")
        else:
            for product in products:
                print(f"\nНазвание продукта: {product[0]}")
                print(f"Категория: {product[1]}")
                print(f"Цена: {product[2]}")
                print(f"Количество на складе: {product[3]}")


while True:
    show_stores(db_name)
    store_id = input("\nВведите ID магазина (0 для выхода): ")

    if store_id == "0":
        print("Выход из программы.")
        break

    if store_id.isdigit():
        store_id = int(store_id)
        show_products_by_store(db_name, store_id)
    else:
        print("Ошибка! Введите корректный ID магазина.")



