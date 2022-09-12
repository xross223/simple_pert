import plotly
plotly.__version__

import plotly.graph_objects as go
import plotly.figure_factory as ff
from datetime import datetime
from plotly.subplots import make_subplots

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-01', Resource='Apple'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Grape'),
      dict(Task="Job C", Start='2009-04-20', Finish='2009-09-30', Resource='Banana')]

colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)']

figg = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True)
figg.show()

figs = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,
    subplot_titles =('Gantt', 'Scatter')
)

for trace in figg.data:
    figs.add_trace(trace, row=1, col=1)

trace_row2 = go.Scatter(x=[datetime(2009, 1, 1), datetime(2009, 9, 30)],
                         y=[1, 3], marker_color='blue', line_color='blue')
figs.add_trace(trace_row2, row=2, col=1)

#figg.layout

figs.update_layout(width = 900, height=600,
                   xaxis_showticklabels=True)#modify the attributes in figs.layout.xaxis
                                             #that are different in figg.layout.xaxis
figs.update_layout(xaxis= figg.layout.xaxis)
#if we change the order of the following two lines the yaxis_domain is deleted by the second update, while
#in the xaxis updates above the first update is preserved, WHY?!!!!!!!!!!!!!!!!!
#Moreover my first attempt was  to perform only the first  line update, for figs.layout.yaxis,
#supposing that the initial figs.layout.yaxis attributes are preserved, but in this case they also disappeared
figs.update_layout(yaxis=figg.layout.yaxis);
figs.update_layout(yaxis_domain= [0.625, 1.0], yaxis_anchor='x')
figs.show()