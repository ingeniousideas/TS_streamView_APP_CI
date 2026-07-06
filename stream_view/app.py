import dash
from dash import Dash, html, dcc, dash_table
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc

load_figure_template(["cyborg", "darkly"])

# Initialize the Dash app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sidebar layout
sidebar = html.Div(
    [
        html.H2("Pages", className="sidebar-header"),
        html.Hr(),
        # Dynamically create links for each page
        dbc.Nav(
            [
                dbc.NavLink(
                    page["name"], href=page["path"], active="exact"
                ) for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

# Main app layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=2),  # Sidebar takes 2 columns width
                dbc.Col(
                    # Page content rendered here
                    dash.page_container,
                    width=10
                )
            ]
        )
    ],
    fluid=True
)

# The app will be served by Gunicorn
server = app.server  # Expose Flask server for Gunicorn
