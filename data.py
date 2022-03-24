import plotly.figure_factory as ff
import pandas as pd
import csv
df = pd.read_csv("C:/Users/gogof/OneDrive/Desktop/coding/hi-main/c108/project/data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["average ratin"],show_hist=False)
fig.show()