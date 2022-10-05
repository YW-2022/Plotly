import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]

layout = go.Layout(title="Hello first Plotly", 
					xaxis={'title':'My x axis'}, 
					yaxis=dict(title='My x axis'),
          hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter1.html')
