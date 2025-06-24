import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# barplot => to display categorical data
df = pd.DataFrame({'Cat':['A','B','C','D'], 'Value':[10,20,30,40]})
plt.bar(df['Cat'],df['Value'])
plt.show()
sns.barplot(x='Cat',y='Value',data=df)
plt.show()
# stacked barplot => to display cummulative data (seaborn doesnt support this)
df1 = pd.DataFrame({'Cat':['A','B','C','D'], 'Value1':[10,20,30,40], 'Value2':[5,6,7,8]})
plt.bar(df1['Cat'],df1['Value1'],label='Value1')
plt.bar(df1['Cat'],df1['Value2'],bottom='Value1',label='Value2')
plt.legend()
plt.show()
# grouped barplot => allows comparison bet/ween multiple subcategories within categories
df2 = pd.DataFrame({
'Category': ['A', 'A', 'B', 'B'],
'Subcategory': ['X', 'Y', 'X', 'Y'],
'Values': [10, 15, 7, 12]
})
pivot_df = df2.pivot(index='Category',columns='Subcategory',values='Values') # matploylib
pivot_df.plot(kind='bar')
# we use pivot to changre the structure of the dataframe
plt.show()
sns.catplot(x='Category',y='Values',hue='Subcategory',data=df2,kind='bar')
plt.show()
# histogram => grouping of cont data into bins
df3 = pd.DataFrame({'Values': [10,20,30,40,50,60,70,80,90]})
plt.hist(df3['Values'], bins=5)
plt.show()
sns.histplot(df3['Values'], bins=5)
plt.show()
# piechart => to show the proportion of each category in relation to the whole (seaborn doesnt support)
plt.pie(df['Value'],labels=df['Cat'],autopct='%1.1f%%') # %1.1f%% rounds off 22.45 to 22.5
plt.show()
# line chart => dispalys trends overtime
df4 = pd.DataFrame({"x":[1,8,3],"y":[4,9,6]})
plt.plot(df4['x'],df4['y'])
plt.show()
sns.lineplot(x='x',y='y',data=df4)
plt.show()
# Scatter plot => shows the relationship between two continuous variables.
plt.scatter(df4['x'],df4['y'])
sns.scatterplot(x='x',y='y',data=df4)
plt.show()
# boxplot => to display the distribution of data, showing quartiles and outliers
plt.boxplot(df3['Values'])
sns.boxplot(y='Values',data=df3)
plt.show()