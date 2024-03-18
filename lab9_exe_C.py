"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
Name: lab9_exe_C.py
Assignment: Lab 9, Exercise C
Author(s): Sofia Tapias, Tanis Smith
Submission: March 18, 2024
Description: Fetch data by Python.
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
import requests
import json

def fetch_product_data (url):
    try:
        response = requests.get(url)
        # Raises an error for bad responses
        response.raise_for_status ()
        # The JSON structure includes a ' products ' key
        return response . json () [ ' products ']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: { e }")
        return None

def list_all_products(products):
# complete this function
    return
    
def search_product(products, name):
    for product in products:
    # complete the for loop ,
    # it must pretty print the product details with 4 indents
        print("Product not found.")
    return

def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            choice = input("Choose an option:\n 1.List all products\n 2.Search for a product\n 3.Exit\n>")
            if choice == '1 ':
            # complete the code .
            # call suitable function ( s )
            elif choice == '2 ':
                product_name = input (" Enter the product name : ")
                # complete the code .
                 # call suitable function ( s )
            elif choice == '3 ':
                 break
            else:
                 print (" Invalid choice . Please try again .")
    else:
         print (" Failed to fetch product data .")