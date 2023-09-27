'''
This file contains the Database class that handles the MySQL database operations.
'''
import mysql.connector
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        self.cursor = self.connection.cursor()
    def save_data(self, name, product):
        query = "INSERT INTO customers (name, product) VALUES (%s, %s)"
        values = (name, product)
        self.cursor.execute(query, values)
        self.connection.commit()
    def get_sales_metrics(self):
        query = "SELECT AVG(sales) as average_sales, COUNT(*) as total_sales FROM sales"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
    def get_customer_satisfaction(self):
        query = "SELECT COUNT(*) as total_customers, SUM(satisfaction) as total_satisfaction FROM customers"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
    def close_connection(self):
        self.cursor.close()
        self.connection.close()