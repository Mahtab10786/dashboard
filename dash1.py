import pandas as pd
import streamlit as st
import json
import plotly.express as px
from PIL import Image

st.set_page_config(page_title=' VISUALISATION OF DASHBOARD  ')

st.header('jason data')
jd=open('jsondata.json')
data=json.load(jd)
for i in data['intensity']
  print(i)
  jd.close()
  
  
  topic=df['topic'].unique().tolist()
  country=df['country'].unique().tolist()
  enddate=df['end date'].unique().tolist()
  
  st.header('filter here')
  topic_selection=st.multiselect('topic:',topic, default=topic)

 enddate_selection=st.multiselect('enddate:',enddate, default=enddate)  
  
 country_selection=st.multiselect('country:',country, default=country)
 
 bar_chart=px.bar(jd,x='country',y='enddate')
 st.plotly_chart(bar_chart)
 
 pie_chart=px.pie(jd,title='production wise',value='production',names='enddate')
 st.plotly_chart(pie_chart)
