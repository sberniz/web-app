# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
app_pipe = load('assets/dating.joblib')
import pandas as pd
import dash_table
from collections import OrderedDict
# Imports from this application
import app
from app import app,X_test,dating_df2
from joblib import load
app_pipe = load('assets/dating.joblib')
#from app import app
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

column1 =  dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        html.P('Select the Options below to get an estimate person relationship status'), 
        dcc.Markdown('#### age'), 
        dcc.Input(
            id='age', 
            type="number",
            placeholder="18",
            value=18,
            className='mb-5 input'
        ), 
        html.Div(id='age-output-container',style={'padding-bottom': 40}),
        dcc.Markdown('#### Income (use -1 for unknown)'), 
        dcc.Input(
            id='income', 
            type="number",
            placeholder="-1",
            value=-1,
            className='mb-5 input'
        ), 
        html.Div(id='income-output-container',style={'padding-bottom': 40}),
        dcc.Markdown('#### Location (city,state or city,country'),         
        dcc.Input(
            id='location', 
            type="text",
            placeholder="San Jose, California",
            value="San Jose, California",
            className='mb-5 input'
        ), 
        html.Div(id='location-output-container',style={'padding-bottom': 40}),

        dcc.Markdown('#### Body Type'), 
        dcc.Dropdown(
            id='body_type', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['body_type'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['body_type'].iloc[0] 
        ),
        dcc.Markdown('#### Diet'), 
        dcc.Dropdown(
            id='diet', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['diet'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['diet'].iloc[0] 
        ),
         dcc.Markdown('#### Drinks'), 
        dcc.Dropdown(
            id='drinks', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['drinks'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['drinks'].iloc[0] 
        ),
        dcc.Markdown('#### Drugs'), 
        dcc.Dropdown(
            id='drugs', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['drugs'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['drugs'].iloc[0] 
        ),
        dcc.Markdown('#### Education'), 
        dcc.Dropdown(
            id='education', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['education'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['education'].iloc[0] 
        ),
        dcc.Markdown('#### Ethnicity'), 
        dcc.Dropdown(
            id='ethnicity', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['ethnicity'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['ethnicity'].iloc[0] 
        ),   
        dcc.Markdown('#### Job'), 
        dcc.Dropdown(
            id='job', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['job'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['job'].iloc[0] 
        ),   
        dcc.Markdown('#### Offspring'), 
        dcc.Dropdown(
            id='offspring', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['offspring'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['offspring'].iloc[0] 
        ),   
        dcc.Markdown('#### Orientation'), 
        dcc.Dropdown(
            id='orientation', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['orientation'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['orientation'].iloc[0] 
        ),
        dcc.Markdown('#### Pets'), 
        dcc.Dropdown(
            id='pets', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['pets'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['pets'].iloc[0] 
        ),
        dcc.Markdown('#### Religion'), 
        dcc.Dropdown(
            id='religion', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['religion'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['religion'].iloc[0] 
        ),
        dcc.Markdown('#### Sex'), 
        dcc.Dropdown(
            id='sex', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['sex'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['sex'].iloc[0] 
        ),
        dcc.Markdown('#### Zodiac Sign'), 
        dcc.Dropdown(
            id='sign', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['sign'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['sign'].iloc[0] 
        ),
        dcc.Markdown('#### Smokes ?'), 
        dcc.Dropdown(
            id='smokes', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['smokes'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['smokes'].iloc[0] 
        ),
        dcc.Markdown('#### languages'), 
        dcc.Dropdown(
            id='speaks', 
            options = [
                {'label': i, 'value': i}
                    for i in dating_df2['speaks'].unique()
            ],  
            className='mb-5',
            clearable=False,
            value=dating_df2['speaks'].iloc[0] 
        ),
    ],
    md=4,
)
column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Relationship Status

            Relationship Status with Selected Features

            """
        ),
        html.Div(id='prediction-content', className='lead')
        
    ],
    md=4,
)

@app.callback(
    dash.dependencies.Output('age-output-container', 'children'),
    [dash.dependencies.Input('age', 'value')])
def update_output(value):
    return html.Strong('Age:',style={'padding':0}),' {} years old'.format(value)
@app.callback(
    dash.dependencies.Output('income-output-container', 'children'),
    [dash.dependencies.Input('income', 'value')])
def update_output2(value):
    return html.Strong('Income:',style={'padding':0}),' {} /year'.format(value)
@app.callback(
    dash.dependencies.Output('prediction-content', 'children'),
    [dash.dependencies.Input('age', 'value'),
    dash.dependencies.Input('body_type', 'value'),
    dash.dependencies.Input('diet', 'value'),
    dash.dependencies.Input('drinks', 'value'),
    dash.dependencies.Input('drugs', 'value'),
    dash.dependencies.Input('education', 'value'),
    dash.dependencies.Input('ethnicity', 'value'),
    dash.dependencies.Input('income', 'value'),
    dash.dependencies.Input('job', 'value'),
    dash.dependencies.Input('location', 'value'),
    dash.dependencies.Input('offspring', 'value'),
    dash.dependencies.Input('orientation', 'value'),
    dash.dependencies.Input('pets', 'value'),
    dash.dependencies.Input('religion', 'value'),
    dash.dependencies.Input('sex', 'value'),
    dash.dependencies.Input('sign', 'value'),
    dash.dependencies.Input('smokes', 'value'),
    dash.dependencies.Input('speaks', 'value')])
def predict(age, body_type, diet, drinks, drugs, education, ethnicity,
       income, job, location, offspring, orientation, pets,
       religion, sex, sign, smokes, speaks):
    Model_Year = body_type 
    Electric_Range = age
    df = pd.DataFrame(
        columns=['age', 'body_type', 'diet', 'drinks', 'drugs', 'education', 'ethnicity',
       'income', 'job', 'location', 'offspring', 'orientation', 'pets',
       'religion', 'sex', 'sign', 'smokes', 'speaks'],
        data=[[age, body_type, diet, drinks, drugs, education, ethnicity,
       income, job, location, offspring, orientation, pets,
       religion, sex, sign, smokes, speaks]]
    )
    y_pred = app_pipe.predict(df)[0]
    
    print(y_pred)
    return f'{y_pred}'



layout = dbc.Row([column1, column2])
