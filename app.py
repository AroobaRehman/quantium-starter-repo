from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv('output/sales.csv')
df = df.sort_values(by="date")

linechart = px.line(df,x='date', y='sales',line_shape='spline',
        color_discrete_sequence=['#1aa37a'])

regions = [str(region) for region in df['region'].unique()]

app.layout = html.Div([

    html.H1('Pink Morsel Sales', id = 'app-header'),

    dcc.Graph(
        id='sales-graph',
        figure=linechart
    ),
    html.Br(),

    html.Div("Select a Region:", className="section-label"),

    html.Div([
        dcc.RadioItems(regions, 'north', inline=True, id="radio-item",className ='radio-buttons')
    ], className='radio-group'
    )

    
])

@callback(
    Output('sales-graph','figure'),
    Input('radio-item', 'value'),)

def update_figure(selected_region):
    df_region = df[df['region'] == selected_region].copy()
    linechart = px.line(df_region,x='date', y='sales',line_shape='spline',
        color_discrete_sequence=['#1aa37a'])


    return linechart


    

if __name__ == '__main__':
    app.run(debug=True)
