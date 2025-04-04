# Исходные данные для заполнения таблиц
import csv

import psycopg2

#
# # connect to database
# conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='genri123$')
# try:
#     with conn:
#         with conn.cursor() as cur:
#
#             # execute query
#             cur.execute("INSERT INTO user_account VALUES (%s, %s)", (7, "Nikolay"))
#             cur.execute("SELECT * FROM user_account")
#
#             rows = cur.fetchall()
#
#             for row in rows:
#                 print(row)
# finally:
#     conn.close()
#
# def fill_table_from_csv(table_name, file_name):
#     conn = psycopg2.connect(dbname='courses', user='postgres', password='genri123$', port='5432', host='localhost')
#     cursor = conn.cursor()
#
#     with open(file_name) as csv_file:
#         csv_reader = csv.reader(csv_file)
#         header = next(csv_reader)
#         for row in csv_reader:
#             query = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ({', '.join(["%s"] * len(row))})"
#             cursor.execute('SET DateStyle = "ISO, MDY";')
#             cursor.execute(query, row)
#
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# def main() -> None:
#     fill_table_from_csv('students', '../data/sqlstudents.csv')
#     fill_table_from_csv('courses', '../data/courses.csv')
#     fill_table_from_csv('instructors', '../data/instructors.csv')
#
#
# if __name__ == "__main__":
#     main()


with open("../data/customers_data.csv", newline="") as file:
    customers_data = [row for row in csv.reader(file) if "customer_id" not in row]

with open("../data/employees_data.csv", newline="") as file:
    employees_data = [row for row in csv.reader(file) if "first_name" not in row]

with open("../data/orders_data.csv", newline="") as file:
    orders_data = [row for row in csv.reader(file) if "order_id" not in row]

# Создайте подключение к базе данных
conn = psycopg2.connect(dbname="analysis", user="simple", host="sql_db", port="5432", password="qweasd963")

# Открытие курсора
cur = conn.cursor()

# Не меняйте и не удаляйте эти строки - они нужны для проверки
cur.execute("create schema if not exists itresume14744;")
cur.execute("DROP TABLE IF EXISTS itresume14744.orders")
cur.execute("DROP TABLE IF EXISTS itresume14744.customers")
cur.execute("DROP TABLE IF EXISTS itresume14744.employees")


# Ниже напишите код запросов для создания таблиц
cur.execute(
    """
CREATE TABLE itresume14744.customers (
    customer_id CHAR(5) PRIMARY KEY NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
)
"""
)

cur.execute(
    """
CREATE TABLE itresume14744.employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(35) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT
)
"""
)

cur.execute(
    """
CREATE TABLE itresume14744.orders (
    order_id INT PRIMARY KEY NOT NULL,
    customer_id CHAR(5) NOT NULL,
    employee_id INT NOT NULL,
    order_date DATE NOT NULL,
    ship_city VARCHAR(100) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
)
"""
)

# Зафиксируйте изменения в базе данных
conn.commit()

# Теперь приступаем к операциям вставок данных
# Запустите цикл по списку customers_data и выполните запрос формата
# INSERT INTO itresume14744.table (column1, column2, ...) VALUES (%s, %s, ...) returning ", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning

for customer in customers_data:
    query = (
        "INSERT INTO itresume14744.customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s) RETURNING *"
    )
    cur.execute(query, customer)


# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_customers = cur.fetchall()

# Запустите цикл по списку employees_data и выполните запрос формата
# INSERT INTO itresume14744.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
for employee in employees_data:
    query = """
    INSERT INTO itresume14744.employees (first_name, last_name, title, birth_date, notes) 
    VALUES (%s, %s, %s, %s, %s) RETURNING *
    """
    cur.execute(query, employee)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_employees = cur.fetchall()


# Запустите цикл по списку orders_data и выполните запрос формата
# INSERT INTO itresume14744.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
for order in orders_data:
    query = """
    INSERT INTO itresume14744.orders (order_id, customer_id, employee_id, order_date, ship_city) 
    VALUES (%s, %s, %s, %s, %s) RETURNING *
    """
    cur.execute(query, order)


# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_orders = cur.fetchall()

# Закрытие курсора
cur.close()

# Закрытие соединения
conn.close()
