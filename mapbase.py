import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("Covid Portal")
url = r"mapbase/data.csv"
dfa = pd.read_csv(url)
genre = st.radio("What would you like to do? ", ('Feed the Needy', 'Corona Information', 'Emergency Services'))
if genre == 'Feed the Needy':
    dfa1=dfa[dfa["type"]=="Donate"]
    st.text("Here is a list of Agencies supplying food to Needy")
    option = st.selectbox('Select an Agency for More Details',dfa1['Title1'])
    dfa2=dfa1[dfa1["Title1"]==option]
    title=dfa2["Title1"].to_string()
    Subt=dfa2["Subtitle1"].to_string()
    desc=dfa2["Description1"].to_string()
    st.text(title)
    st.text(Subt)
    st.text(desc)
if genre == 'Corona Information':
    dfa1=dfa[dfa["type"]=="Hospital"]
    st.text("Corona Information Brochure")
    st.image("mapbase/img1.jpeg")
if genre == 'Emergency Services':
    dfa1=dfa[dfa["type"]=="Emergency"]
    st.text("Here is a list of Emergency Hospitals for Corona")
    st.write(dfa1[["type","Title1","Subtitle1","Description1"]])    

    
    #option = st.selectbox("Donate | Information | Emergency ", dfa['type'].tolist(), default=dfa['type'].tolist())   
#st.map(dfa3,500)
px.set_mapbox_access_token("pk.eyJ1IjoicmFodWxyYW5qYW5zcml2YXN0YXZhIiwiYSI6ImNrNWUyMGw0ZjF1aTEzbXJmeGNlaTFwdHkifQ.Mxxle7NdCvAt5R_AWmAXVA")
#set the geo=spatial data
fig = px.scatter_mapbox(dfa1, text="Title1", lat="lat",  hover_name="Subtitle1", hover_data=["Subtitle1","Description1"], lon="lon", size="lat", color="type", zoom=10)
st.write(fig)
