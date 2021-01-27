import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
##IMPORTERS
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.model_selection import RandomizedSearchCV, train_test_split
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, LogisticRegressionCV, LogisticRegression,Ridge,RidgeCV
from scipy import stats
from category_encoders import OneHotEncoder, OrdinalEncoder
import plotly.express as px
from sklearn.preprocessing import StandardScaler


import dash
import dash_bootstrap_components as dbc

dating_df = pd.read_csv('dating_csv.csv')
dating_df2 = dating_df.fillna('unknown')

#XG Boost Regression with early stopping and hyper parameter tuning, best model , will be deployment for post/apptop if the score hasn't improved in 50 rounds
#Pipeline for app
#y_pred = app_pipe.predict(X_test)[0]
external_stylesheets = [
    dbc.themes.BOOTSTRAP, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
    'style.css' #for slider
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True # see https://dash.plot.ly/urls
app.title = 'Relationship Status Predictor <Just for Fun>' # appears in browser title bar
server = app.server