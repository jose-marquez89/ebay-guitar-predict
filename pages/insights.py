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
        html.H2("Insights"),
        
        dcc.Markdown(
			"""
        
			The following table illustrates something called 
			[permutation importance](https://www.kaggle.com/dansbecker/permutation-importance),
			which helps us see how our machine learning model is making
			predictions. Comprehensive understanding of permutation 
			importance isn't necessary to gain insight here: The country 
			your guitar is made in and the brand are the two biggest 
			influencers on the predictive model's decisions.
			
			"""
        ),
        html.Img(src='assets/pi-weights.png', className='img-fluid'),
        html.Br(),
        html.Div([
			html.Br(),
			html.P(
			"""
			The next two graphs are called partial dependence plots.
			The line represents change in prediction based on 
			adjusting the feature's value. In the graph below, predictions
			are either positively or negatively affected by changing 
			your guitar brand from say, a Peavey to a Gibson.
			"""),
			html.Img(src='assets/brand_pdp.png', className='img-fluid')
		]),
		html.Br(),
		html.Div([ 
			dcc.Markdown(
			"""
			In the chart below, you can see how an exclusive change in
			the country of manufacture drives price prediction up or
			down from a baseline.
			"""),
			html.Img(src='assets/country_pdp.png', className='img-fluid')
		])
		
    ],
    md=10
)

layout = dbc.Row([column1])
