'''
This file contains the Metrics class that calculates and displays sales metrics.
'''
from database import Database
import matplotlib.pyplot as plt
class Metrics:
    def display_metrics(self):
        database = Database()
        sales_metrics = database.get_sales_metrics()
        customer_satisfaction = database.get_customer_satisfaction()
        database.close_connection()
        average_sales = sales_metrics[0]
        total_sales = sales_metrics[1]
        total_customers = customer_satisfaction[0]
        total_satisfaction = customer_satisfaction[1]
        # Code to display sales metrics graphically
        labels = ['Average Sales', 'Total Sales']
        values = [average_sales, total_sales]
        plt.bar(labels, values)
        plt.xlabel('Metrics')
        plt.ylabel('Values')
        plt.title('Sales Metrics')
        plt.show()
        satisfaction_percentage = (total_satisfaction / total_customers) * 100
        print(f"Customer Satisfaction: {satisfaction_percentage}%")