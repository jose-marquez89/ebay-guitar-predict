# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from app import app
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set df's for dist plots
price = pd.read_csv('data/price.csv')
y = price['Price'].values
y_log = np.log1p(y)

# df for sample table
sample = pd.read_csv('data/guitar-sample.csv')

# Price visualizations
y_data = [y_log]
y_label = ['Log Dollars']
fig = make_subplots(rows=2, cols=1)
trace0 = go.Histogram(x=y, name='Dollars')
trace1 = go.Histogram(x=y_log, name='Log Dollars')
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 2, 1)

def generate_table(dataframe):
	return html.Table(
		# Header
		[html.Tr([html.Th(col) for col in dataframe.columns])] +
		
		# Body
		[html.Tr([
			html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
		]) for i in range(len(dataframe))]
	)

# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [	
		html.H2("Process"),
        dcc.Markdown(
            """
            
            How does the app make it's predictions? First, data from 
            eBay sold and completed listings is funneled into a structure
            called a dataframe. This labeled table contains thousands
            of rows of individual **samples**, or individual sales
            observations. The data has a ton of missing values, 
            incorrect spellings, unnecessary columns and a myriad of
            other things to clean up. After the data is tidied up, it
            will look like the table below. This formatted data
            will be fed to the machine learning model.


            """
        ),

    ],
    md=12
)


column2 = dbc.Col([
		html.Div(children=[
			html.H4(children='Guitar Data, Source: eBay'),
			generate_table(sample)
			]
		)
	],
	md=12		
)

column3 = dbc.Col([
		html.Br(),
		html.H4("Accounting For Right Skewed Data"),
		dcc.Markdown(
			"""
			The *target* or the thing we want to predict is the Price
			column. Usually, when predicting from a normal, bell-shaped
			distribution curve (like a collection of basketball player
			heights, for example) we can take the average, and use that
			to derive the [mean absolute error](https://en.wikipedia.org/wiki/Mean_absolute_error).
			However, with prices ranging from 99 cents to $10k, it can
			really throw off our model, which is ultimately regression
			based. To rectify this, the target of Price is transformed
			to a logarithmic scale. The graphs to the right illustrate
			our two differing distributions. The blue graph ranges from
			below 1 to 10k, like our real-life prices, while the red 
			graph shows a more normal distribution. The 
			logarithmic transformation compresses larger numbers and
			inflates smaller ones, revealing insights that were not 
			apparent before.
			""")
	],
	md=6		
)

column4 = dbc.Col([
		
		dcc.Graph(id='dollars-dist', figure=fig)
	],
	md=6
)

column5 = dbc.Col([
		html.H4("The Machine Learning Model"),
		dcc.Markdown(
			"""
			After the data is prepped and the prices are transformed, 
			the data can be used to "train" a machine learning model.
			In the case of this app, the model is one produced with
			a technique known as [gradient boosting]
			(https://en.wikipedia.org/wiki/Gradient_boosting). This 
			technique uses an ensemble of weaker prediction models, 
			known as [decision trees]
			(https://en.wikipedia.org/wiki/Decision_tree_learning).
			On a fundamental level, boosting takes these weak learners
			and uses many of them to create one, significantly 
			strengthened learner, analogous to a "wisdom of crowds" 
			situation. The model is then validated against a smaller
			subset of the data, in order to test the size of it's error, 
			in this case, measured in Mean Absolute Error. This process 
			is repeated until the error can no longer be reasonably
			improved by more iterations. When this process is complete,
			we get our final model, which can make predictions that
			often beat even an educated guess!
			""")])

layout = [dbc.Row([column1]),
		  dbc.Row([column2]),
		  dbc.Row([column3, column4]),
		  dbc.Row([column5])]
