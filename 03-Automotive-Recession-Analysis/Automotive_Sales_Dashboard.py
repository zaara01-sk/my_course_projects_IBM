#!/usr/bin/env python
# coding: utf-8

"""
Automotive Sales Statistics Dashboard

This Dash application provides an interactive visualization of automobile sales data.
It allows users to analyze historical trends and compare sales performance during
recession periods versus non-recession periods.

Features:
1. Comparison of automobile sales during recession periods.
2. Analysis of vehicle type performance trends.
3. Interactive year-based sales reports.
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# --- Data Loading ---
# Load the dataset
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Automobile Statistics Dashboard"

# --- Layout Configuration ---
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
year_list = [i for i in range(1980, 2024, 1)]

app.layout = html.Div([
    # Dashboard Title
    html.H1("Automobile Sales Statistics Dashboard",
            style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 24}),

    # Dropdown Menu: Report Type
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value='Yearly Statistics',
            placeholder='Select a report type',
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlign': 'center'}
        )
    ], style={'width': '80%', 'margin': '20px auto'}),

    # Dropdown Menu: Year Selection
    html.Div([
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select a year',
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlign': 'center'}
        )
    ], style={'width': '80%', 'margin': '20px auto'}),

    # Graphs Display Area
    html.Div(id='output-container', className='chart-grid',
             style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'})
])

# --- Callbacks ---

# Callback 1: Enable/Disable Year Dropdown based on Report Type
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    else:
        return True

# Callback 2: Update Graphs based on selection
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):
    
    if selected_statistics == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]

        # 1. Average Sales fluctuation over Recession Period
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                           title='Average Automobile Sales Fluctuation over Recession Period')
        )

        # 2. Average Vehicles Sold by Vehicle Type
        avg_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(avg_sales, x='Vehicle_Type', y='Automobile_Sales',
                          title='Average Vehicles Sold by Vehicle Type during Recession')
        )

        # 3. Total Expenditure Share by Vehicle Type
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type',
                          title='Total Advertising Expenditure Share by Vehicle Type')
        )

        # 4. Effect of Unemployment Rate on Vehicle Type and Sales
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data, x='unemployment_rate', y='Automobile_Sales', color='Vehicle_Type',
                          title='Effect of Unemployment Rate on Sales by Vehicle Type')
        )

        return [
            html.Div(className='chart-item', children=[html.Div(R_chart1), html.Div(R_chart2)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(R_chart3), html.Div(R_chart4)], style={'display': 'flex'})
        ]

    elif selected_statistics == 'Yearly Statistics' and input_year:
        yearly_data = data[data['Year'] == input_year]

        # 1. Yearly Automobile Sales (Overall trend reuse)
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas, x='Year', y='Automobile_Sales', title='Yearly Automobile Sales Trend')
        )

        # 2. Total Monthly Sales for the Selected Year
        monthly_sales = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(monthly_sales, x='Month', y='Automobile_Sales',
                           title=f'Total Monthly Automobile Sales in {input_year}')
        )

        # 3. Average Vehicles Sold by Vehicle Type
        avg_vehicle = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avg_vehicle, x='Vehicle_Type', y='Automobile_Sales',
                          title=f'Average Vehicles Sold by Type in {input_year}')
        )

        # 4. Total Advertisement Expenditure
        ad_exp = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(ad_exp, values='Advertising_Expenditure', names='Vehicle_Type',
                          title=f'Total Advertisement Expenditure in {input_year}')
        )

        return [
            html.Div(className='chart-item', children=[html.Div(Y_chart1), html.Div(Y_chart2)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(Y_chart3), html.Div(Y_chart4)], style={'display': 'flex'})
        ]
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)