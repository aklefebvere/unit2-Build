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
            # What is the dataset?
            The dataset I used was published on Kaggle and I took that dataset and imported it locally so I can work with it.

            This is what the raw dataset looks like:
            """
        ),

        html.Img(src='assets/raw_dataset.png', className='img-fluid'),

        dcc.Markdown(
            """
            This dataset consists of cars located in India. Each car in the dataset gives you some information about that car such as the fuel type of the car and the model year of the car. The price column in the dataset is in lakh. Lakh is a
            unit used in the Indian numbering system which equals 100,000 Indian Rupees. Just by the looks of the raw dataset, this dataset needs quite a bit cleaning in order for this to be implemented into a predictive model.

            # Data Cleaning
            Before I started cleaning, I split the dataset into three parts: train, validation, and test. These separate datasets will be used to help me find the best predictive model for this dataset. Each split was a 80%, 20% split which means
            80 percent of data will be used for the train and 20% of the dataset will be used for validation and test.

            This is what the shape looks like for each dataset split:
            """
        ),

        html.Img(src='assets/dataset_splits.png', className='img-fluid'),

        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            "Unnamed: 0" and "New_Price" columns needs to be dropped since it shows no relevency towards the data. In order for this to be used properly in a predictive model, all the columns must match their data type (Categorical columns must by objects
            and int/float columns must be numeric columns). Mileage, engine, and Power columns have their units assigned for each cell which must be removed so it can be a numeric column. All the cars that had the fuel type CNG, LPG, and electric
            were dropped from the dataset because it did not follow the mileage units that the majority of the dataset was using

            Before I start implementing my dataset into a predictive model, I checked to see if there was a skew on my target variable "Price".

            Graph of target variable "Price":
            '''
        ),

        html.Img(src='assets/without_log.png', className='img-fluid'),

        dcc.Markdown(
            '''
            By the looks of it, there is skew on the target variable

            We can remove this skew by taking the 8th root of the target values to minamize the outliers shown here:
            '''

        ),

        html.Img(src='assets/with_log.png', className='img-fluid'),

        dcc.Markdown(
            '''
            Now that the target outliers are improved, we can now implement the dataset into predictive models.

            # Predictive Model Implementation

            ## XGBoost Regressor
            For XGBoost Regressor, I used ordinal encoding to encode my categorical variables. Rather than using an imputer to replace my NaN values, I did it by hand to prevent any problems from happening when visualizing my model.
            I also did not use a pipeline to create my model because XGBoost does not like being inside a pipeline.

            This is my validation accuracy once fitting my train dataset and predicting my validation r^2 score:

            '''
        ),

        html.Img(src='assets/XGB_val.png', className='img-fluid'),

        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            This is my test accuracy once fitting my train and validation datasets combined and predicting my test score:
            '''
        ),

        html.Img(src='assets/XGB_test.png', className='img-fluid'),

        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            ## Random Forest Regressor
            For random forest regressor, I used ordinal encoding and imputed every NaN value with its mean and implemented everything inside a pipeline including the random forest class.
            '''
        ),

        html.Img(src='assets/pipeline.png', className='img-fluid'),

        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            This is my validation accuracy once fitting my train dataset and calculating my validation r^2 score:
            '''
        ),
        
        html.Img(src='assets/RFR_val.png', className='img-fluid'),

          html.Br(),
          html.Br(),

        dcc.Markdown(
            '''
            This is my test accuracy once fitting my train dataset and calculating my test r^2 score:
            '''
        ),

        html.Img(src='assets/RFR_test.png', className='img-fluid'),

        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            ## Linear Regression
            For Linear regression, I fit my train onto the model and calculated my r^2 score for my validation and test dataset. I didn't do much with this because based on my previous scores from the other models, I can tell that this is
            never going to beat my XGBoost regressor model or my random forest regressor model.

            This is my validation accuracy once fitting my train dataset and calculating my validation r^2 score:
            '''     
        ),

        html.Img(src='assets/LR_val.png', className='img-fluid'),

        html.Br(),
        html.Br(),

         dcc.Markdown(
            '''
            This is my test accuracy once fitting my train dataset and calculating my test r^2 score:
            '''
        ),

        html.Img(src='assets/LR_test.png', className='img-fluid'),

        html.Br(),
        html.Br(),

         dcc.Markdown(
            '''
            ## What Predictive Model Did I Choose?

            By looking at all the test accuracys for each model, XGBoost regressor has the highest test accuracy but I will be using the random forest regression model instead. The reason why I am selecting random forest over XGBoost is
            because my random forest regressor model is in a pipeline and it would be much easier to work with. Random forest regressor is still a valid model to use since the test accuracys between XGBoost and random forest are not
            significantly different.
            '''
        ), 

    ],
)

layout = dbc.Row([column1])