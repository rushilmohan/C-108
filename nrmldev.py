import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

df = pd.read_csv("data.csv")

abc = ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating"],show_hist=False)
abc.show()

print(df["Avg Rating"].tolist())