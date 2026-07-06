import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px

"""
TODO: get_data_gapminder() is called on every page load and every graph update,
		fine for development,
		add caching,
			(e.g. functools.lru_cache or Dash's diskcache)
		for production.
"""
# app data module
from data.data_API_212_pies import get_data_pies, get_data_gapminder
import layouts.pies_table as pies_table

dash.register_page(__name__, path="/", name="Admin", order=0)


def layout():
	df_gap = get_data_gapminder()
	pies_data = get_data_pies()

	return html.Div([
			html.Div([
				
				# Page header
				html.H1(children='TradeStream-SteamView', style={'textAlign':'center'}),

				# drop down menu
				html.Div([
					dcc.Dropdown(df_gap.country.unique(), 'Canada', id='dropdown-selection'),
				]),

				# line graph
				html.Div([
					dcc.Graph(id='graph-content'),
				], className='graph-container'),

				# pies data table
				html.Div([
					pies_table.create_table(pies_data),
				]),
	
			])
		],className='main-content')

# callbacks are what bind the components inputs and outputs together. These are decorators on the following funciont (def).
@callback(
	Output('graph-content', 'figure'),
	Input('dropdown-selection', 'value')
)
def update_graph(value):
	df_gap = get_data_gapminder()
	dff = df_gap[df_gap.country==value]
	return px.line(dff, x='year', y='pop')