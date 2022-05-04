from unicodedata import name
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df_2 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df_f1 = pd.read_csv('f1-predictor/03_s3/race_results.csv')

fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

fig2 = px.line(df_2, x='City', y='Amount', color='Fruit')

fig3 = px.line(df_f1, x='raceName', y='cumPoints', color='driverId')

app.layout = html.Div(children=[
    html.H1(children='Hello World'),

    html.Div(children='''
        Dash: A web application framework for you data.
    ,'''),

    dcc.Graph(
        id='example-graph',
        figure=fig3
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)