# visualization.py
import plotly.express as px

def render_visualization(df, visualization_type, sidebar):
    if visualization_type == "Bar Chart":
        x_axis = sidebar.selectbox("Select X-axis", df.columns)
        y_axis = sidebar.selectbox("Select Y-axis", df.columns)
        fig = px.bar(df, x=x_axis, y=y_axis)
        
    elif visualization_type == "Line Chart":
        x_axis = sidebar.selectbox("Select X-axis", df.columns)
        y_axis = sidebar.selectbox("Select Y-axis", df.columns)
        fig = px.line(df, x=x_axis, y=y_axis)
        
    elif visualization_type == "Pie Chart":
        names = sidebar.selectbox("Select Category", df.columns)
        values = sidebar.selectbox("Select Values", df.columns)
        fig = px.pie(df, names=names, values=values)
        
    elif visualization_type == "Heatmap":
        fig = px.imshow(df.corr(), text_auto=True)
        
    elif visualization_type == "Scatter Plot":
        x_axis = sidebar.selectbox("Select X-axis", df.columns)
        y_axis = sidebar.selectbox("Select Y-axis", df.columns)
        fig = px.scatter(df, x=x_axis, y=y_axis)
        
    else:
        fig = None
    
    return fig
