# pandas: used for data manipulation(analyzing, cleaning)
import pandas as pd
myseries = [1,2,3,4,5,6,7,8,9]
Series = pd.Series(myseries)
print("Series: ", Series) # series:1d array in pandas, labels are indices unless they are specified
myvar = pd.Series(myseries, index=['a','b','c','d','e','k','g','h','i'])
print('custon labels: ', myvar)
dictdata = {'key1': 'value1', 'key2':'value2'} # dict as series
print('dict as series: ', pd.Series(dictdata))
print('dict as series with custom keys: ', pd.Series(dictdata, index=['key1']))
mydata ={
    'name':['himasri','pranathi','rashmitha'],
    'age':['21','21','21'],
    'location':['hyd','mokila','mncl'],
    'height':[5.3,5.2,5.8]
}
data = pd.DataFrame(mydata) # dataframes are multi dimentional tables 
print('DATAFRAME data: ', data)
print("1st row in Df: ", data.loc[0])
# print("returns only 1st 5 rows: ", pd.read_csv('data.csv))
# print("returns only 1st 5 rows: ", pd.read_csv('data.csv))
# to dispaly 99999 rows => pd.options.display.max_rows = 99999 # print("returns 99999 rows: ", pd.read_csv('data.csv))
# use  pd.read_csv('data.csv).to_string() to print entire dataset
# print("returns only 1st 5 rows: ", pd.read_json ('data.json))
# for custon no.of rows=> from top => data.head(10)
# for custon no.of rows=> from bottom => data.tail(10)
# more info abt dataset => data.info()
# df = pd.read_csv('path')
# df.dropna(inplace = True) => generally dropna is used for removing null rows it creates new dataset but using inplace
# as true the originally dataset values are changed. df.dropna(axis=1) => removes null columns
# pd.fillna(100, inplace = True) => fills null value with 100
# x = df['column_name].mean() / x = df['column_name].median() / x = df['column_name].mode()[0]
# df.fillna({'row_name": x, inplace = True})
# fixing format => df['Date] = pd.to_datetime(df['Date'], formate='mixed')
# df.dropna(subset = ['Date'], inplace = True)
# replace values => 
# for x in df.index:
#   if df.loc[x, 'Duration']>120:
#     df.loc[x, 'Duration'] = 120 / drop rows => df.drop(x, inplace = True)
# remove duplicates => df.drop_duplicates(inplace = true) 
# df.corr() => defines correlation of the numeric data of the dataset=> good corr (>0.6(directly prop) and <-0.6(inverserly propotional))               

# data visualization using matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0.0,5.0,250)
# print(x)
plt.figure(figsize=(8,5))
plt.hist(x,bins=30,color='pink',edgecolor='green') #histogram: to display continuous data  
plt.title('Histogram of x')
plt.xlabel('value')
plt.ylabel('frequency')
plt.grid(False)
# plt.show()
# barplot: fpor displaying categorical data as rectangular bars