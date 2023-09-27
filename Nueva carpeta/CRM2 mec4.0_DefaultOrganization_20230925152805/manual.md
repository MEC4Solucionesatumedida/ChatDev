# ChatDev CRM User Manual

## Introduction

Welcome to the ChatDev CRM user manual! This manual will guide you through the installation process, introduce you to the main functions of the software, and provide instructions on how to use it effectively.

## Installation

To install the ChatDev CRM, please follow the steps below:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the ChatDev CRM repository from GitHub using the following command:

   ```
   git clone https://github.com/chatdev/crm.git
   ```

3. Navigate to the cloned repository:

   ```
   cd crm
   ```

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you are ready to use the ChatDev CRM!

## Main Functions

The ChatDev CRM provides the following main functions:

1. Interaction with users through WhatsApp: The CRM includes a chatbot that interacts with users through WhatsApp. It uses ChatGPT to generate responses and collects basic customer information and product/service details.

2. Database integration: The CRM is integrated with a MySQL database. It saves the customer information, product/service details, and user ratings in the database for future reference.

3. Rating system: At the end of the interaction, the CRM requests a rating from the user to evaluate the service provided. The rating is saved in the database.

4. Metrics system: The CRM includes a metrics system that calculates and displays consolidated metrics. It shows the average sales values, total sales count, and customer satisfaction percentage.

## Usage

To use the ChatDev CRM, follow the steps below:

1. Run the `main.py` file using the following command:

   ```
   python main.py
   ```

2. The CRM will start listening for incoming messages from WhatsApp.

3. When a message is received, the chatbot will process it and extract customer information and product/service details.

4. The extracted information will be saved in the MySQL database.

5. The chatbot will then request a rating from the user.

6. The rating provided by the user will be saved in the database.

7. The metrics system will be updated with the new data from the database.

8. Finally, the consolidated metrics will be displayed.

## Conclusion

Congratulations! You have successfully installed and learned how to use the ChatDev CRM. You can now interact with users through WhatsApp, save customer information in a MySQL database, collect user ratings, and view consolidated metrics. Enjoy using the ChatDev CRM to enhance your customer relationship management processes!