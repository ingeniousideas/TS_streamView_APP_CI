import dash
from dash import html

dash.register_page(__name__, path="/home", name="Home", order=1)

methods = [
    'Market fundamentals data analysis',
    'Regression back-tested sentiment analysis of social media and investment analysts',
    'Other mechanisms'
]

layout = html.Div(
    className="page-center-col",
    children=[
        html.Div(
            className="content-wrap",
            children=[
    
        html.Div(
    
            style={"maxWidth": "900px", "width": "100%", "boxSizing": "border-box"},  # Limit the width of content
    
            children=[
    
                html.H1('TradeStream', style={"textAlign": "center"}),  # Center-align header

                # purpose
                html.Div(
                        className="board-heading",
                        children=[
                            html.H2('Purpose', className='board-title'),
                        ]
                    ),
                    html.Div(
                        className="info-board board-body",
                        children=[
                            html.P('Automate allocation of regular investment and provide visibility of portfolio performance. Also make this deployed with GitHub Actions and ArgoCD'),
                        ]
                    ),

                # aim
                html.Div(
                        className="board-heading",
                        children=[
                            html.H2('Aim', className='board-title'),
                        ]
                    ),
                    html.Div(
                        className="info-board board-body",
                        children=[
                            html.P('Develop weighting algorithms to apportion allocation of funds based on:'),
                            html.Ul(
                                id='method-list',
                                className='method-list',
                                children=[html.Li(i) for i in methods]
                            ),
                        ]
                    ),

                # objective
                html.Div(
                        className="board-heading",
                        children=[
                            html.H2('Objective', className='board-title'),
                        ]
                    ),
                    html.Div(
                        className="info-board board-body",
                        children=[
                            html.P('Create an income stream through strategic profit taking whilst still growing a balanced portfolio.'),
                        ]
                    ),
            ]
        ),
    ]
)])