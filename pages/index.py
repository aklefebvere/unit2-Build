# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Build a car and find its predicted price!

             🚗 With this app, you can build your own car and find it's predicted price with the parameters you select.

             🚘 This app is for people that are interested in how much a car would cost if built and bought in India.

             🏎️ Predictive prices are predicted with a random forest regression model that is built with an r^2 of above 90%. With this high of an r^2, the price will be very close to what the car would actually cost.

            """
        ),
        dcc.Link(dbc.Button('Build your car!', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [
       html.Img(src='assets/car.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])