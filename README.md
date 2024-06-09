# Product Recommendation System

This project is a simple prototype of a product recommendation system, where users can receive recommendations based on their interaction history with products.

## Overview

The recommendation system is designed to suggest products to users by analyzing their interaction history. It tracks user interactions with products and generates recommendations based on user preferences.

## Features

- **User Interaction Tracking:** The system records user interactions with products to understand user preferences.
- **Recommendation Generation:** Based on user interaction history, the system generates product recommendations for users.

## Technologies Used

- **Python:** The project is implemented in Python programming language.
- **NumPy:** NumPy library is used for numerical computations and data manipulation.

## Usage

1. **Clone the Repository:**
   
    https://github.com/sekhar-36/Product-Recommendation-System.git

2. **Navigate to the Project Directory:**
   
    cd product-recommendation-system

3. **Run the Program:**
   
    PRS.py

4. **Follow the On-screen Instructions:**
- Enter the user name.
- Select a product from the provided list.
- View the generated recommendations.

## How it Works

- The system initializes with a list of users and products.
- User interaction frequency matrix is created using NumPy, where rows represent users and columns represent products.
- The `reclist` function generates recommendations for a given user based on their interaction history.
- The `viewproduct` function allows users to interact with products by updating the interaction frequency matrix.

## Contributing

Contributions are welcome! If you want to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Make sure to follow the project's coding style and guidelines.
