# code_snippet
```python
st.image("logo.png")
```
```
import plotly.graph_objects as go

fig = go.Figure()

# Adding a scatter plot (or any other trace)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))

# Adding annotations
fig.update_layout(
    annotations=[
        go.layout.Annotation(
            x=2,             # x position of annotation
            y=5,             # y position of annotation
            text="Point (2,5)", # Text to display
            showarrow=True,   # Show an arrow pointing to the annotation
            arrowhead=2,      # Arrowhead style
            ax=0,             # X offset for the arrow's tail
            ay=-40            # Y offset for the arrow's tail
        )
    ]
)

fig.show()
```
