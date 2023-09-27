from chatbot import Chatbot
from database import Database
from metrics import Metrics
# Create instances of the classes
chatbot = Chatbot()
database = Database()
metrics = Metrics()
# Receive a message from WhatsApp
message = chatbot.receive_message()
# Process the message and extract customer and product/service information
customer_info, product_info = chatbot.process_message(message)
# Save the customer and product/service information in the database
database.save_data(customer_info, product_info)
# Request a rating from the user
rating = chatbot.request_rating()
# Save the rating in the database
database.save_rating(rating)
# Update the metrics system with the new data from the database
metrics.update_metrics(database)
# Display the consolidated metrics
metrics.display_metrics()