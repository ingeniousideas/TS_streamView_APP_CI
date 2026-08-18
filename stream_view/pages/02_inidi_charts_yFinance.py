import dash
import pandas as pd
import plotly.express as px
import pytz
import yfinance as yf
from dash import Input, Output, callback, dcc, html

dash.register_page(__name__, path="/charts_indi_yfinance", name="Charts - Individual (yFinance)", order=2)

layout = html.Div([

		html.Div([

			# Page header
			html.H1(children='TradeStream Individual Asset Time Series Charts', style={'textAlign':'center'}),

			# yfinance aero graph components
			html.Div([

				# Line graph section
				html.Div([
				
					# Header title
					html.H2("Aerospace Giants"),

					# Option dropdown
					dcc.Dropdown(
						id='aero_selection',
						options=[
							{'label': 'Rolls-Royce (RR)', 'value': 'RR.L'},
							{'label': 'Airbus (AIR)', 'value': 'AIR.PA'},
							{'label': 'BAE Systems (BA)', 'value': 'BA.L'},
							{'label': 'Tesla (TSLA)', 'value': 'TSLA'},
							{'label': 'IBM (IBM)', 'value': 'IBM'},
							{'label': 'Microsoft (MSFT)', 'value': 'MSFT'},
							{'label': 'NVIDIA (NVDA)', 'value': 'NVDA'},
							{'label': 'BP (BP.L)', 'value': 'BP.L'},
							{'label': 'Vodafone (VOD.L)', 'value': 'VOD.L'},
							{'label': 'TCS (TCS.NS)', 'value': 'TCS.NS'},
							{'label': 'Sony (SONY)', 'value': 'SONY'},
							],
						value='RR.L',  # Default ticker
						placeholder="Select a stock ticker"
					),
				]),

				# Graph
				html.Div([
				
					html.H2(id='', className='', children='Asset Price Chart'),
					# Graph
					dcc.Graph(id='aero_graph'
					),

				], className='graph-container'),

				# control buttons
				html.Div([
					html.H2(id='', className='', children='Asset Graph Control Buttons'),
					# Update button
					html.Button('Update Graph', id='update-button'),
				]),

			]),

		])

	],className='main-content')

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)

    # Fetch history first — more robust than fast_info
    hist = stock.history(period="2y")
    hist.reset_index(inplace=True)

    if hist.empty:
        raise ValueError(f"No data returned for {symbol}")

    # Get timezone from the data itself if possible, otherwise fall back to fast_info
    if 'Date' in hist.columns and pd.api.types.is_datetime64_any_dtype(hist['Date']):
        tz_info = hist['Date'].dt.tz
        timezone = tz_info.zone if tz_info is not None else stock.fast_info.get('timezone', 'UTC')
    else:
        timezone = stock.fast_info.get('timezone', 'UTC')

    return hist, timezone

def preprocess_stock_data(symbol):
	""" Add features to the dataframe.
		- Format date.
		- Add percentage bands.
	"""

	stock_data = fetch_stock_data(symbol=symbol)
	df = stock_data[0]
	ticker_timezone = stock_data[1]

	if df.empty:
		return pd.DataFrame()  # Return an empty DataFrame if no data

	# Ensure 'Date' is timezone-aware and convert to the ticker's timezone
	df['Date'] = pd.to_datetime(df['Date'])

	if df['Date'].dt.tz is None:
		df['Date'] = df['Date'].dt.tz_localize('UTC')
	df['Date'] = df['Date'].dt.tz_convert(ticker_timezone)

	# Filter to the last 52 calendar weeks
	today = pd.Timestamp.now(pytz.timezone(ticker_timezone))
	start_date = today - pd.Timedelta(weeks=52)
	df = df[df['Date'] >= start_date]

	# Calculate 52-week moving average
	df['52_Week_MA'] = df['Close'].rolling(window=252, min_periods=1).mean()
	df['26_Week_MA'] = df['Close'].rolling(window=126, min_periods=1).mean()

	percentages = [0.1, 0.2, 0.3]
	for p in percentages:
		df[f'Close +{int(p*100)}%'] = df['Close'] * (1 + p)
		df[f'Close -{int(p*100)}%'] = df['Close'] * (1 - p)

	for p in percentages:
		df[f'52_Week_MA +{int(p*100)}%'] = df['52_Week_MA'] * (1 + p)
		df[f'52_Week_MA -{int(p*100)}%'] = df['52_Week_MA'] * (1 - p)

	return df

def build_graph(df, symbol):
	# Create the base figure
	fig = px.line(title=f'{symbol} Asset Prices with Market Timezone')

	# Add stock price line
	fig.add_scatter(x=df['Date'], y=df['Close'],
				 	mode='lines', name='Stock Price',
				 	line={"color": 'white', "width": 1}
				 	)

	# Add 52-week moving average line
	fig.add_scatter(x=df['Date'], y=df['52_Week_MA'],
				 	mode='lines', name='52-Week MA',
				 	line={"dash": 'dash', "color": 'blue', "width": 1}
				 	)

	# Add selected percentage bands
	percent_bands: list = [0.1,0.2,0.3]
	for band in percent_bands:

		line_width = int(band*10)

		fig.add_scatter(x=df['Date'], y=df[f'52_Week_MA +{int(band*100)}%'],
				  		mode='lines', name=f'{int(band*100)}%',
						line={"dash": 'dot', "color": 'green', "width": line_width}
						)

		fig.add_scatter(x=df['Date'], y=df[f'52_Week_MA -{int(band*100)}%'],
		  				mode='lines', name=f'-{int(band*100)}%',
						line={"dash": 'dot', "color": 'red', "width": line_width}
						)


	# Customize x-axis to display dates
	fig.update_xaxes(
		title_text='Date',
		tickformat='%b %d, %Y',
		showgrid=True
	)

	return fig

# Callback for updating the graph
@callback(
	Output('aero_graph', 'figure'),
	Input('aero_selection', 'value'),
)
def update_aero(selected_dropdown_value):

	# Fetch and preprocess stock data
	df_stock_timeseries = preprocess_stock_data(selected_dropdown_value)
	if df_stock_timeseries.empty:
		return {}

	# Build the graph
	fig = build_graph(df_stock_timeseries, selected_dropdown_value)

	return fig

# Callback for updating the graph
@callback(
	Output('tech_graph', 'figure'),
	Input('tech_selection', 'value'),
)
def update_tech(selected_dropdown_value):

	# Fetch and preprocess stock data
	df_stock_timeseries = preprocess_stock_data(selected_dropdown_value)
	if df_stock_timeseries.empty:
		return {}

	# Build the graph
	fig = build_graph(df_stock_timeseries, selected_dropdown_value)

	return fig