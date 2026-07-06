import dash
from dash import dcc, html

from data.data_API_alphaVantage import extract_data, create_stock_price_figure

# app layouts module
import layouts.alpha_table as alpha_table

# data api import
from data.data_API_alphaVantage import alpha_get_ibm

dash.register_page(__name__, path="/charts_indi_alpha", name="Charts - Individual (alphaVantage)", order=3)

# Sample API response data
data = {
    'Meta Data': {
        '1. Information': 'Intraday (5min) open, high, low, close prices and volume',
        '2. Symbol': 'IBM',
        '3. Last Refreshed': '2024-10-23 19:55:00',
        '4. Interval': '5min',
        '5. Output Size': 'Compact',
        '6. Time Zone': 'US/Eastern'
    },
    'Time Series (5min)': {
        '2024-10-23 19:55:00': {'1. open': '226.7500', '2. high': '226.9500', '3. low': '226.3000', '4. close': '226.9500', '5. volume': '3396'},
        '2024-10-23 19:50:00': {'1. open': '226.6800', '2. high': '226.9500', '3. low': '226.6500', '4. close': '226.6500', '5. volume': '1401'},
        '2024-10-23 19:45:00': {'1. open': '226.7000', '2. high': '226.7000', '3. low': '226.6000', '4. close': '226.6500', '5. volume': '43'},
        '2024-10-23 19:40:00': {'1. open': '226.6900', '2. high': '226.7000', '3. low': '226.2500', '4. close': '226.3000', '5. volume': '58'},
        '2024-10-23 19:35:00': {'1. open': '225.9900', '2. high': '226.7000', '3. low': '225.9800', '4. close': '226.2501', '5. volume': '5670'},
        '2024-10-23 19:30:00': {'1. open': '225.7600', '2. high': '225.9900', '3. low': '225.7000', '4. close': '225.9900', '5. volume': '484'},
        '2024-10-23 19:25:00': {'1. open': '225.7000', '2. high': '226.0000', '3. low': '225.7000', '4. close': '225.9900', '5. volume': '97'},
        '2024-10-23 19:20:00': {'1. open': '225.7000', '2. high': '225.7100', '3. low': '225.7000', '4. close': '225.7000', '5. volume': '351'},
        '2024-10-23 19:15:00': {'1. open': '225.7165', '2. high': '226.0000', '3. low': '225.7000', '4. close': '225.7000', '5. volume': '422'},
        '2024-10-23 19:10:00': {'1. open': '225.7500', '2. high': '225.9999', '3. low': '225.7000', '4. close': '225.7500', '5. volume': '1244'}
    }
}

# data = alpha_get_ibm()
data = data

# Extract data
timestamps, closing_prices = extract_data(data)
symbol = data['Meta Data']['2. Symbol']

# Create figure
figure = create_stock_price_figure(timestamps, closing_prices, symbol)


layout = html.Div([
			html.Div([
				
				# Page header
				html.H1(children=f"Stock Prices for {symbol}", style={'textAlign':'center'}),

				# line graph
				html.Div([
					    dcc.Graph(
                        id='stock-price-graph',
                        figure=figure),
				], className='graph-container'),
	
		],
		className='main-content'
		)
	])