import dash
from dash import html

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
                    className="board-heading",
                    style={
                        "marginTop": "20px",
                        "marginBottom": "10px"
                    },
                    children=[
                        html.H2('Overview'),
                    ]
                ),
                html.Div(
                    className="info-board board-body",
                    children=[
                        html.P('Admin page for TradeStream.'),
                        html.P('Highlights the responsibilities and processes for Admin users.'),
                    ]
                ),

                # activities
                html.Div(
                    className="board-heading",
                    style={
                        "marginTop": "20px",
                        "marginBottom": "10px"
                    },
                    children=[
                        html.H2('Activities'),
                    ]
                ),
                html.Div(
                    className="info-board board-body",
                    children=[
						html.P('Administer the application and manage user accounts.'),
                    	html.P('Monitor system performance and logs.'),
						html.P('Configure application settings and preferences.'),	
                    ]

                ),
                
            ]
        ),
    ]
)
