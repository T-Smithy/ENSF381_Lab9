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
        response.raise_for_status()
        # The JSON structure includes a 'products' key
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def list_all_products(products):
    print("\nProduct List:\n")
    for product in products:
        print("     ", product['title'])
    print("\n")
    return

'''
This function utilizes a for loop in order to iterate over all of the entires in the JSON file, 
and using the key value of 'title' each of the items name are printed. we also added \n in order to aid
with the spacing when the items are being printed out 
'''
    
def search_product(products, name):
    print()
    for product in products:
    # complete the for loop ,
    # it must pretty print the product details with 4 indents
        #Source for info on pretty print: https://www.digitalocean.com/community/tutorials/python-pretty-print-json
        if product['title']== name:
            formatted_product = json.dumps(product, indent=4)
            print(formatted_product, "\n")
            return
    print("Product not found.\n")
    return

'''
this functions utilizes the key in order to retrun all of the attributes 
associated with it, calling all of them instead of having a singular call 
for each of teh attributes. It iterates over each of the entires in the JSON file
using a for loop, coparing these values to the name of the product being searched
the loops end at the last product and if there is no match it prints item not fount
'''

def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            choice = input("Choose an option:\n 1.List all products\n 2.Search for a product\n 3.Exit\n>")
            if choice == '1':
                # complete the code .
                list_all_products(products)
            elif choice == '2':
                product_name = input ("Enter the product name: ")
                # complete the code .
                search_product(products, product_name)
            elif choice == '3':
                 break
            else:
                 print("Invalid choice. Please try again.")
    else:
         print("Failed to fetch product data.")

if __name__ == "__main__":
    main()