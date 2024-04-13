import plotly.graph_objects as go

# Create a scatter plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 20]
scatter = go.Scatter(x=x, y=y)

# Create a plot
fig = go.Figure()
fig.add_trace(scatter)
fig.show()
