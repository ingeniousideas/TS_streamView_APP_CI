from dash import dash_table

def create_table(data):
    # Dynamically extract column headers from the first item in the data
    columns = [{"name": col, "id": col} for col in data[0].keys()]

    return dash_table.DataTable(
        id='pies-table',
        columns=columns,
        data=data,
        sort_action="native",
        style_table={'overflowX': 'auto'},
        style_cell={
            'backgroundColor': '#333',
            'color': '#f0f0f0',
            'minWidth': '150px',
            'width': '150px',
            'maxWidth': '150px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
        style_header={
            'backgroundColor': '#444',
            'fontWeight': 'bold',
            'color': '#f0f0f0',
        },
        style_data={
            'backgroundColor': '#333',
            'color': '#f0f0f0',
        }
    )