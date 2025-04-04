import psycopg2
import csv
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

def fill_table_from_csv(table_name, file_name):
    conn = psycopg2.connect(dbname='courses', user='postgres', password='genri123$', port='5432', host='localhost')
    cursor = conn.cursor()

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            query = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ({', '.join(["%s"] * len(row))})"
            cursor.execute('SET DateStyle = "ISO, MDY";')
            cursor.execute(query, row)

    conn.commit()
    cursor.close()
    conn.close()

def main() -> None:
    fill_table_from_csv('students', '../data/sqlstudents.csv')
    fill_table_from_csv('courses', '../data/courses.csv')
    fill_table_from_csv('instructors', '../data/instructors.csv')


if __name__ == "__main__":
    main()
