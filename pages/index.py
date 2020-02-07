import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## How Much Will eBayers Pay?

            Despite MSRP's, guitars often sell for unexpected prices 
            on one of the world's largest online marketplaces. These 
            prices are unlikely to be driven by normal market 
            expectations.

            The individual attributes of an electric guitar
            can sway the minds and emotions of guitar buyers on eBay.

            This app uses
            [**Machine Learning**]
            (https://en.wikipedia.org/wiki/Machine_learning) 
            to predict electric guitar resale prices.

            """
        ),
        dcc.Link(
			dbc.Button('Predict Resale Price', color='primary'), 
			href='/predictions'
		)
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/man-browsing-at-a-guitar-shop.jpg', 
				 className='img-fluid'),
        html.P(
			children=[
				"Photo by: ",
				html.A("Jinnifer Douglass",
					href="https://burst.shopify.com/@ji_n_yc?utm_campaign="\
                         "photo_credit&amp;utm_content=Free+Man+Browsing+At"\
                         "+A+Guitar+Shop+Photo+%E2%80%94+High+Res+Pictures&"\
                         "amp;utm_medium=referral&amp;utm_source=credit",
                         
			    )
			]
		)
	],
	md=8
)

layout = dbc.Row([column1, column2])
