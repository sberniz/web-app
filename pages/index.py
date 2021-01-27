# Imports from 3rd party libraries
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app,dating_df2

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        ## Predict Relationship Status

           """
        ),
        dcc.Link(dbc.Button('Predict Status', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [
                dcc.Markdown(
            """
        ## Predict Relationship Status

           """
        ),
    ]
)

layout = dbc.Row([column1, column2])