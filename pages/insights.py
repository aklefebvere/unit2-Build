# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
# Imports from this application
from app import app
import pandas as pd
import plotly.express as px

df = pd.read_csv('assets/train')

# fig = go.Figure(data=[go.Scatter(x=df['Power_bhp'], y=df['Price_Lakh'])])

fig = px.scatter(df, 'Power_bhp', 'Price_Lakh')
fig2 = px.scatter(df, 'Year', 'Price_Lakh')
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

            To see the correlation between the price and the top two features, we can create a scatter plot of the two features:

            Power_bhp plot:
            """
        ),

        dcc.Graph(
            figure=fig
        ),

        html.Br(),

        dcc.Markdown(
            '''
            Year of car plot:
            '''
        ),

        dcc.Graph(
            figure=fig2
        ),

        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            Plotting the top two features against each other:
            '''
        ),

        html.Img(src='assets/pdp_interact.png', className='img-fluid'),

        dcc.Markdown(
            '''
            The two scatterplots above show that there is a positive correlation between the two features and the target. The scatterplots were created with just the train dataset without the target being converted to the 8th root due
            to limitations with plotly express.
            The interative partial dependence plot shows that when year and power of the car increases, the price of the car increases.

            We can also visualize if a feature in the model is increasing the predicted price or decreasing the predicted price with a shapley plot: 
            '''
        ),

        html.Img(src='assets/shap.png', className='img-fluid'),

        dcc.Markdown(
            '''
            With this shapley plot, every feature in the red is increasing the predicited price and every feature in the blue is decreasing the predicted price. Location is increasing the predicted price the most and power is decreasing
            the predicted price the most.
            '''
        )
        
    ],
)

layout = dbc.Row([column1])