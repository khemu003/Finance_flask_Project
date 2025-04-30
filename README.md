# Personal Finance Dashboard

## Overview
The Personal Finance Dashboard is a web application designed to help users manage their personal finances effectively. It allows users to track their income and expenses, providing a comprehensive view of their financial health.

## Features
- **User  Registration and Authentication**: Secure login and registration with password hashing for data protection.
- **Transaction Management**: Perform Create, Read, Update, and Delete (CRUD) operations on financial transactions.
- **User  Engagement**: Contact and feedback forms to gather user insights and improve the application.

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Libraries**: 
  - bcrypt for password hashing
  - pandas for data handling

## Installation
Clone the repository:

    git clone https://github.com/khemu003/personal-finance-dashboard.git

    cd personal-finance-dashboard

Install the required packages:

    pip install -r requirements.txt

Set up the environment variables in a `.env` file:

    SECRET_KEY=your_secret_key

    host=your_database_host
    
    user=your_database_user
    
    password=your_database_password
    
    name=your_database_name
    
    port=your_database_port
   
Run the application:
    
    python app.py

## Usage
- Navigate to `http://localhost:5000` in your web browser.
- Register a new account or log in with existing credentials.
- Manage your transactions and provide feedback through the forms available.
