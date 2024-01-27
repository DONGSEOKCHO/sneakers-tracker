from dash import Dash, html, dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from wordcloud import WordCloud          # pip install wordcloud

# Build Layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6('Total Sneakers'),
                    html.Br(),
                    html.H1(id='part-count', style={'margin-left': "15px"}),
                    html.H6(id='total-count', style={'textAlign': 'center', 'opacity': 0.5}),
                ])
            ], style={"height": 200}),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6('Mean Retail Price'),
                            html.Br(),
                            html.H3(id='price-retail')
                        ])
                    ], style={"height": 200})
                ])
            ])
        ], width=2),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6('Mean Volatility'),
                    html.Br(),
                    html.H3(id='mean-vola')
                ])
            ], style={"height": 200}),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6('Mean Increase'),
                            html.Br(),
                            html.H3(id='total-inc')
                        ])
                    ], style={"height": 200})
                ]),
            ],)
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5('All Sneakers'),
                    dcc.Dropdown(
                        id = 'pandas-dropdown-1',
                        options = ["Price", "Volatility"], 
                        value= "Price",
                        style={"width": "40%"},
                        clearable=False,                      
                    ),  
                ])
            ]),
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id='bar-chart', 
                        figure={
                            "layout" : {
                            "height": 290,
                        }}, 
                        config={'displayModeBar': False},
                        style={"maxHeight": "290px", "overflow-y": "scroll"},
                        ),
                    
                ],)
            ])
        ]),
    ], className='p-2 align-items-stretch'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label('Highest Price'),
                    dcc.RangeSlider(0, 4100, value=[0, 4100], allowCross=False, id='price-slider'), 
                ])
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.Label('Increased Amount'),
                    dcc.RangeSlider(-50, 4000, value=[-50, 4000], allowCross=False, id='increase-slider')
                ])
            ]),
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src="/assets/StockX tags.jpg", 
                        top=True,
                        className="img-fluid rounded-start",
                        style={'height':'40%', 'width':'100%', 'display': 'block', 'margin-left': 5, 'margin-right': 5}
                ),
                ])
            ]),
            
        ], width=2, style={"height": '100%'}),
       
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div(children=[
                        html.Div([
                            html.Label(['Brand']),
                            dcc.Dropdown(
                                id = 'pandas-dropdown-2',     
                                clearable=False,  
                            ), 
                        ], style={"width": "33%", "margin-left": "10px", "font-size": "85%"}),
                        html.Div([
                            html.Label(['Model']),
                            dcc.Dropdown(
                                id='pandas-dropdown-3',
                                clearable=False, 
                                disabled=False                  
                            ),  
                        ], style={"width": "33%", "margin-left": "20px", "font-size": "85%"}),
                        html.Div([
                            html.Label(['Size']),
                            dcc.Dropdown(                                
                                id ='pandas-dropdown-4',
                                clearable=False, 
                                disabled=False 
                            ),
                        ], style={"width": "33%", "margin-left": "20px", "font-size": "85%"})
                    ],style=dict(display='flex')),
                    
                ]),
            ]),
            dbc.Col([
                dbc.Row([
                    # dbc.Card([
                    #     dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png", 
                    #                 top=True,
                    #                 className="img-fluid rounded-start",
                    #                 style={'height':'40%', 'width':'100%', 'display': 'block', 'margin-left': 5, 'margin-right': 5}
                    #     ),
                    #     dbc.CardBody([
                    #         dcc.Graph(
                    #             id='line-chart', 
                    #             figure={
                    #                  "layout" : {
                    #                 "height": 195,
                    #                 }
                    #             }, 
                    #             config={'displayModeBar': False},
                    #     ),
                    #     ], style={"padding-top": 0, "padding-bottom": 0},)
                    # ], style={"height": 300, "width": 250},)
                ], style={"width": "100%"}, id="output"),
            ], style={"maxHeight": "60vh", "overflow-y": "scroll"})
        ]),
    ]),    
], fluid=True)


