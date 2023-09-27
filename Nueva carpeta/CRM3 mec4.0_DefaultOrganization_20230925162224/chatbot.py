'''
This file contains the Chatbot class that interacts with the users via WhatsApp using ChatGPT.
'''
class Chatbot:
    def interact(self, name, product):
        # Code to interact with ChatGPT and return response
        response = f"Hello {name}, thank you for using our CRM application. You have requested information about {product}. How can I assist you further?"
        return response