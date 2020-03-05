# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            # Insights
            We can see the importance of each feature in the model by looking at the permutation importance r^2 score:
            """
        ),

        html.Img(src='assets/PI_graph.png', className='img-fluid'),

        dcc.Markdown(
            """
            We can see here that the two most important features towards the model is the power of the car and the model year of the car. You may have also noticed that there are three features that have zero r^2 score. They have no importance
            towards the model but it does affect the model when removed  do to potentially the noise it creates by just being in the dataset.
            """
        ),


    ],
)

layout = dbc.Row([column1])