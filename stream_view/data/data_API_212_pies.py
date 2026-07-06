import pandas as pd
import json

def get_data_pies():

    # Sample JSON data (replace this with your actual data)
    data_input = [
    	{"id": 1, "name": "Item 1", "price": 9.99, "quantity": 10},
    	{"id": 2, "name": "Item 2", "price": 19.99, "quantity": 5},
    	{"id": 3, "name": "Item 3", "price": 29.99, "quantity": 15}
    ]

    # Check if the data is already a list or a JSON string
    if isinstance(data_input, str):
        # If it's a string, try to parse it as JSON
        data = json.loads(data_input)
    elif isinstance(data_input, list):
        # If it's a list, use it as-is
        data = data_input
    else:
        raise ValueError("Input data must be a JSON string or a list")

    return data

def get_data_gapminder():

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

    return df