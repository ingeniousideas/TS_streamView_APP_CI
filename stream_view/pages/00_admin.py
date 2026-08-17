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


layout = html.Div(
    
    style={"display": "flex", "flexDirection": "column", "alignItems": "center", "padding": "20px"},  # Center the content
    
    children=[
    
        html.Div(
    
            style={"maxWidth": "900px", "width": "100%", "boxSizing": "border-box"},  # Limit the width of content
    
            children=[
    
                html.H1('TradeStream', style={"textAlign": "center"}),  # Center-align header

                # admin overview
                html.Div(
                    className="admin_view",
                    style={
                        "marginTop": "20px",
                        "marginBottom": "10px"
                    },
                    children=[
                        html.H2('Overview'),
                    ]
                ),
                html.Div(
                    className="purpose",
                    style={"padding": "10px", "border": "1px solid #ccc", "borderRadius": "5px"},
                    children=[
                        html.P('Automate allocation of regular investment and provide visibility of portfolio performance. Also make this deployed with GitHub Actions and ArgoCD'),
                    ]
                ),

            ]
        ),
    ]
)
