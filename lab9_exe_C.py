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


