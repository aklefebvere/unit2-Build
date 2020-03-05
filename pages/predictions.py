# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
import pandas as pd

pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [   
        html.Label('Transmission'),
         dcc.Dropdown(
            id='Transmission',
            options=[
                {'label': 'Automatic', 'value': 'Automatic'},
                {'label': 'Manual', 'value': 'Manual'}
            ],
            value='Manual',
            searchable=False,
            className='mb-4',
            placeholder="Transmission"
        ),

        html.Label('Fuel Type'),
        dcc.Dropdown(
            id='Fuel_Type',
            options=[
                {'label': 'Petrol', 'value': 'Petrol'},
                {'label': 'Diesel', 'value': 'Diesel'}
            ],
            value='Petrol',
            searchable=False,
            className='mb-4',
            placeholder="Fuel Type"
        ),

        html.Label('Location'),
        dcc.Dropdown(
            id='Location',
            options=[
                {'label': 'Kochi', 'value': 'Kochi'},
                {'label': 'Jaipur', 'value': 'Jaipur'},
                {'label': 'Delhi', 'value': 'Delhi'},
                {'label': 'Mumbai', 'value': 'Mumbai'},
                {'label': 'Coimbatore', 'value': 'Coimbatore'},
                {'label': 'Kolkata', 'value': 'Kolkata'},
                {'label': 'Pune', 'value': 'Pune'},
                {'label': 'Hyderabad', 'value': 'Hyderabad'},
                {'label': 'Bangalore', 'value': 'Bangalore'},
                {'label': 'Chennai', 'value': 'Chennai'},
                {'label': 'Ahmedabad', 'value': 'Ahmedabad'},
            ],
            value='Kochi',
            searchable=False,
            className='mb-1',
            placeholder="Location"
        ),
        
        # html.Label('Owner Type'),
        # dcc.Dropdown(
        #     id='Owner_Type',
        #     options=[
        #         {'label': 'First', 'value': 'First'},
        #         {'label': 'Second', 'value': 'Second'},
        #         {'label': 'Third', 'value': 'Third'},
        #         {'label': 'Fourth & Above', 'value': 'Fourth & Above'}
        #     ],
        #     value='None',
        #     searchable=False,
        #     className='mb-4',
        #     placeholder="Owner Type"
        # ),

        html.Br(),

        html.Label('Year of Car'),

        html.Br(),

        dcc.Input(
            id='Year',
           value=2017,
           type='number',
           className='mb-4'
        ),

        html.Br(),

        html.Label('Mileage'),

        html.Br(),

        dcc.Input(
            id='Mileage',
            value=19.10,
            type='number',
            className='mb-4'    
        ),

        html.Br(),

        html.Label('Engine Displacement'),

        html.Br(),

        dcc.Input(
            id='Engine',
            value=1197.0,
            type='number',
            className='mb-4'    
        ),

        html.Br(),

        html.Label('Power in bhp'),

        html.Br(),

        dcc.Input(
            id='Power_bhp',
            value=82.0,
            type='number',
            className='mb-4'    
        ),

        html.Br(),
        
        html.Label('km Driven'),

        html.Br(),

        dcc.Input(
            id='Kilometers_driven',
            value=15029,
            type='number',
            className='mb-4'
        ),

        html.Br(),

        html.Label('Number of Seats'),
        dcc.Slider(
            id='Seats',
            min=2,
            max=10,
            value=5,
            marks= {
                2: {'label': '2 seats'},
                3: {'label': '3'},
                4: {'label': '4'},
                5: {'label': '5'},
                6: {'label': '6'},
                7: {'label': '7'},
                8: {'label': '8'},
                9: {'label': '9'},
                10: {'label': '10 seats'}
            }  
        ),
    ],
    md=4
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            # html.H2('Expected cost', className='mb-5'),
            html.Div('prediction-content', className='lead')
        )
    ],
    md=4
)


@app.callback(
    Output('prediction-content', 'children'),
    [Input('Transmission', 'value'), 
     Input('Fuel_Type', 'value'),
     Input('Location', 'value'),
     Input('Year', 'value'),
     Input('Mileage', 'value'),
     Input('Engine', 'value'),
     Input('Power_bhp', 'value'),
     Input('Kilometers_driven', 'value'),
     Input('Seats', 'value')]
)

def predict(Location, Year, Kilometers_driven, Fuel_Type, Transmission, Mileage, Engine, Power_bhp, Seats):
    df = pd.DataFrame(
        columns=['Location', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Mileage', 'Engine', 'Power_bhp', 'Seats'],
        data = [[Location, Year, Kilometers_driven, Fuel_Type, Transmission, Mileage, Engine, Power_bhp, Seats]]
    )
    y_pred = pipeline.predict(df)[0]
    return y_pred**8

layout = dbc.Row([column1, column2])