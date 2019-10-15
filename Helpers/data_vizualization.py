import cufflinks as cf
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
  
cf.go_offline()
init_notebook_mode(connected=True)

def plot_timeserie(timeserie, title, xaxis, yaxix):
    '''
    Plot a time series
    
    Parameters:
    - timeserie: time series to be plotted
    - titulo: the title of the chart
    - xaxis: x-axis title
    - yaxix: y-axis title
    '''
    
    layout = go.Layout(
        autosize=False,
        width  = 650,
        height = 500,
        title  = title,
        xaxis  = dict(title=xaxis),
        yaxis  = dict(title=yaxix)
    ) 
    
    timeserie.iplot(title=title, layout=layout)