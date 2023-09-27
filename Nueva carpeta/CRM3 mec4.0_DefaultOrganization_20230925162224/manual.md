# ChatDev CRM User Manual

## Introduction

Welcome to the user manual for ChatDev CRM! This software is a Customer Relationship Management (CRM) tool that allows you to interact with users via WhatsApp using a chatbot powered by ChatGPT. It helps you manage customer data, track product/service requests, and gather customer feedback. Additionally, it provides metrics to analyze sales performance and customer satisfaction.

## Table of Contents

1. Installation
2. Setting Up the Environment
3. Using the CRM Application
4. Metrics and Analytics

## 1. Installation

To install ChatDev CRM, follow these steps:

1. Open your terminal or command prompt.
2. Run the following command:

   ```
   pip install chatdev-crm
   ```

   Alternatively, you can use conda:

   ```
   conda install -c conda-forge chatdev-crm
   ```

3. Wait for the installation to complete.

## 2. Setting Up the Environment

Before using ChatDev CRM, you need to set up the environment by configuring the MySQL database and providing the necessary credentials. Follow these steps:

1. Install MySQL on your system if you haven't already. You can download it from the official MySQL website.

2. Create a new MySQL database for ChatDev CRM.

3. Open the `database.py` file in the ChatDev CRM codebase.

4. Replace the following placeholders with your MySQL database credentials:

   - `your_username`: Replace with your MySQL username.
   - `your_password`: Replace with your MySQL password.
   - `your_database`: Replace with the name of the MySQL database you created.

5. Save the changes.

## 3. Using the CRM Application

To use the ChatDev CRM application, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you have the ChatDev CRM codebase.

3. Run the following command to start the application:

   ```
   python main.py
   ```

4. The CRM application window will open.

5. Enter the customer's name in the "Name" field.

6. Enter the product or service requested by the customer in the "Product/Service" field.

7. Click the "Submit" button.

8. The chatbot will interact with the customer and provide a response.

9. The customer's data will be saved in the MySQL database.

10. A message box will display the chatbot's response.

11. Close the application window when you're done.

## 4. Metrics and Analytics

ChatDev CRM provides metrics and analytics to help you analyze sales performance and customer satisfaction. To view the metrics, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you have the ChatDev CRM codebase.

3. Run the following command to view the metrics:

   ```
   python metrics.py
   ```

4. A graphical representation of the sales metrics will be displayed.

5. The customer satisfaction percentage will be printed in the terminal.

6. Close the metrics window when you're done.

## Conclusion

Congratulations! You have successfully installed and used ChatDev CRM. This user manual provided an overview of the installation process, environment setup, and how to use the CRM application. It also explained how to view metrics and analytics. If you have any further questions or need assistance, please reach out to our support team.