import json
import plotly.graph_objects as go
import os

#get data
path = os.path.join(os.getcwd(), "fig.json")
with open(path, "r", ) as json_data:
    fig = go.Figure(json.load(json_data))



import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div([dcc.Graph(id="main-graph", figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)
