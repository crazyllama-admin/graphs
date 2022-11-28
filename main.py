import plotly.express as px
import pandas as pd
​
from dash import Dash, html, dcc, Input, Output
​
​
app = Dash(__name__)
​
​
df = pd.DataFrame({
    'Campaign ID':  ['1844', '1846', '1911', '1845', '1852', '1928', '1854',],
    'Chargebacks':  [470, 233, 151, 97, 95, 57, 50,],
})
​
fig = px.bar(
    df,
    x='Chargebacks',
    y='Campaign ID',
    orientation='h',
    barmode='group',
    text_auto='<5i',
)
fig.update_layout(
    title='Chargebacks by Campaign ID',
    width=800,
    height=600,
    # marker={'color': '#ff0000', 'line': '#00ff00', 'width': 1.5},
    plot_bgcolor='#0000ff',
    paper_bgcolor='#0000ff',
    yaxis={'autorange': 'reversed'},
)
fig.update_traces(
    textposition='outside',
)
​
app.layout = html.Div(children=[
    dcc.Graph(id='chargebacks', figure=fig)
])
​
​
st.plotly_chart(fig, use_container_width=True)
