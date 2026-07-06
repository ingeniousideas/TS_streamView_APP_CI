import requests

import dash
from dash import dcc, html
import plotly.graph_objects as go
from datetime import datetime

ALPHAVANTAGE_API_KEY = "GIFCQK8AUCTCH8QE"

def alpha_get_ibm():
	# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={ALPHAVANTAGE_API_KEY}'
	r = requests.get(url)
	raw_data = r.json()

	return raw_data

def extract_data(data):
	"""
		Extracts timestamps and closing prices from the JSON data.

		Args:
			data (dict): The JSON data containing stock price information.

		Returns:
			tuple: A tuple containing two lists - timestamps and closing prices.
	"""
	timestamps = []
	closing_prices = []

	for timestamp, values in data['Time Series (5min)'].items():
		timestamps.append(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
		closing_prices.append(float(values['4. close']))

	return timestamps, closing_prices

def create_stock_price_figure(timestamps, closing_prices, symbol):
	"""
		Creates a Plotly figure for the stock price line graph.
	
		Args:
			timestamps (list): A list of datetime objects for the x-axis.
			closing_prices (list): A list of closing prices for the y-axis.
			symbol (str): The stock symbol to display in the title.
	
		Returns:
			plotly.graph_objects.Figure: The Plotly figure containing the stock price graph.
	"""
	fig = go.Figure(
		data=go.Scatter(
			x=timestamps,
			y=closing_prices,
			mode='lines+markers',
			name='Close Price'
		)
	)

	fig.update_layout(
		title=f'Stock Prices for {symbol} (Intraday, 5min Interval)',
		xaxis={'title': 'Time'},
		yaxis={'title': 'Price (USD)'},
		template='plotly_dark'
	)

	return fig