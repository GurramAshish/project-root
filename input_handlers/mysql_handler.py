import mysql.connector

def load_mysql_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        database='your_database'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    conn.close()
    return data
