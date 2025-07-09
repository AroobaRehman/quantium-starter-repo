from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv('output/sales.csv')
df = df.sort_values(by="date")

linechart = px.line(df,x='date', y='sales')

app.layout = html.Div(children = [
    html.H1(children = 'Pink Morsel Sales'),
    dcc.Graph(
        id='sales-graph',
        figure=linechart
    )
])

if __name__ == '__main__':
    app.run(debug=True)
