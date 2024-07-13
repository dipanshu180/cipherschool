import pandas as pa
data = {
    'Name' : ['Deep','Mik',"Dip"],
    'Age' :[20,21,22],
    'City' : ['Patna','Mumbai','Punjab']
}
data['Sex']=['M','F',"M"]
# data= data.drop(columns=['Sex'])
print(data)
# pf = pa.DataFrame(data)
# print(pf)

df = pa.read_csv('C:\\Users\dipan\\Downloads\\AWARDS.csv')
# print(df)

print(df.head())
print(df.tail())
print(df.info())#give more information of data
print(df.describe())#Descriptive statics
print(df['YEAR']) #seleccting single column
print(df[['YEAR','TOTAL']]) #seleccting multiple column
print(df[df['TOTAL']>100])#filter
df=df.drop(columns=['TOTAL'])
df=df.drop(index=2)
print(df)
