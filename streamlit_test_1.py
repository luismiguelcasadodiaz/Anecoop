import json
import plotly.graph_objects as go
import os

#get data
path = os.path.join(os.getcwd(), "fig.json")
with open(path, "r", ) as json_data:
    fig = go.Figure(json.load(json_data))


import streamlit as st
st.write(fig)

