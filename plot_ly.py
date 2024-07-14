import pandas as pa
import plotly.express as px
df = pa.read_csv('C:\\Users\dipan\\Downloads\\AWARDS.csv')
print(df.head()) 
fig = px.line(df , x ='YEAR',y='TOTAL',title ='The year of total' , markers=True)
fig = px.bar(df , x ='YEAR',y='TOTAL',title ='The year of total')

fig = px.scatter(df, x = 'GOVT' , y = 'YEAR' , size='TOTAL')
fig.show()
