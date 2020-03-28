import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("Covid Portal")
url = r"./mapbase/mapbase/data.csv"
dfa = pd.read_csv(url)
st.write(dfa)


#st.map(dfa3,500)
px.set_mapbox_access_token("pk.eyJ1IjoicmFodWxyYW5qYW5zcml2YXN0YXZhIiwiYSI6ImNrNWUyMGw0ZjF1aTEzbXJmeGNlaTFwdHkifQ.Mxxle7NdCvAt5R_AWmAXVA")
#set the geo=spatial data


fig = px.scatter_mapbox(dfa, title="type", lat="lat", lon="lon", size="lat", color="type", zoom=10)
#fig = px.scatter_mapbox(dfa, lat="lat", lon="long", color="TotalOrders", size="no_of_days_event_triggered",
 #                 color_continuous_scale=[(0,"red"), (0.2,"yellow"), (0.4,"green"), (1,"black")], size_max=15, zoom=10)
#fig.show()
st.write(fig)
