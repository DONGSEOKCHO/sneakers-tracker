import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd  

from dash import html, Output, Input, State, dcc 
from dash.exceptions import PreventUpdate

from components import home_callbacks,compare_callbacks,explore_callbacks


app = dash.Dash(__name__,use_pages=True,external_stylesheets=[dbc.themes.UNITED, dbc.icons.BOOTSTRAP],suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(children=[
    dash.page_container
])

home_callbacks.get_callbacks(app)
compare_callbacks.get_callbacks(app)
#explore_callbacks.get_callbacks(app)

if __name__ == "__main__":
    app.run_server( port=8051)