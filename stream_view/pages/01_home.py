import dash
from dash import html

dash.register_page(__name__, path="/home", name="Home", order=1)

methods = [
    'Market fundamentals data analysis',
    'Regression back-tested sentiment analysis of social media and investment analysts',
    'Other mechanisms'
]

layout = html.Div(
    
    style={"display": "flex", "flexDirection": "column", "alignItems": "center", "padding": "20px"},  # Center the content
    
    children=[
    
        html.Div(
    
            style={"maxWidth": "900px", "width": "100%", "boxSizing": "border-box"},  # Limit the width of content
    
            children=[
    
                html.H1('TradeStream', style={"textAlign": "center"}),  # Center-align header

                # purpose
                html.Div(
                    className="pur_name",
                    style={
                        "marginTop": "20px",
                        "marginBottom": "10px"
                    },
                    children=[
                        html.H2('Purpose'),
                    ]
                ),
                html.Div(
                    className="purpose",
                    style={"padding": "10px", "border": "1px solid #ccc", "borderRadius": "5px"},
                    children=[
                        html.P('Automate allocation of regular investment.'),
                    ]
                ),

                # aim
                html.Div(
                    className="aim_name",
                    style={
                        "marginTop": "20px",
                        "marginBottom": "10px"
                    },
                    children=[
                        html.H2('Aim'),
                    ]
                ),
                html.Div(
                    className="aim",
                    style={"padding": "10px", "border": "1px solid #ccc", "borderRadius": "5px"},

                    children=[
                        html.P('Develop weighting algorithms to apportion allocation of funds based on:'),
                        html.Ul(
                            id='method-list',
                            style={"listStyleType": "disc", "paddingLeft": "20px"},  # Styling for the list
                            children=[html.Li(i) for i in methods]
                        ),
                    ]
                ),

                html.Div(
                    className="obj_name",
                    style={
                        "marginTop": "20px",
                        "marginBottom": "10px"
                    },
                    children=[
                        html.H2('Objective'),
                    ]
                ),
                html.Div(

                    className="objective",
                    style={"padding": "10px", "border": "1px solid #ccc", "borderRadius": "5px"},
                    children=[
                        html.P('Create an income stream through strategic profit taking whilst still growing a balanced portfolio.'),
                    ]
                ),
            ]
        ),
    ]
)
