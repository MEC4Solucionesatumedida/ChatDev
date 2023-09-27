'''
This file contains the CRMApp class that represents the main application window.
'''
from tkinter import Tk, Label, Button, Entry, messagebox
from chatbot import Chatbot
from database import Database
class CRMApp:
    def __init__(self, master):
        self.master = master
        master.title("CRM Application")
        self.label = Label(master, text="Welcome to the CRM Application!")
        self.label.pack()
        self.name_label = Label(master, text="Name:")
        self.name_label.pack()
        self.name_entry = Entry(master)
        self.name_entry.pack()
        self.product_label = Label(master, text="Product/Service:")
        self.product_label.pack()
        self.product_entry = Entry(master)
        self.product_entry.pack()
        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.database = Database()  # Create an instance of the Database class
    def submit(self):
        name = self.name_entry.get()
        product = self.product_entry.get()
        chatbot = Chatbot()
        response = chatbot.interact(name, product)
        self.database.save_data(name, product)  # Use the instance of the Database class
        messagebox.showinfo("Response", response)
        self.close_connection()  # Close the database connection
    def close_connection(self):
        self.database.close_connection()