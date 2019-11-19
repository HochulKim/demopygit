import pandas as pd
import seaborn as sns

df=sns.load_dataset("iris")
print(df.head(0))
print(df)

columns =['sepal_width','sepal_length','species']
print(df[columns].head())

print("Now")
# print(df['sepal_length'])
# print(df.sepal_length)

print(df.filter(regex ='length$'))
print(df.filter(regex ='^sepal'))
print(df.filter(regex = '^(?!species$).*'))

print(df.loc[2:5,'sepal_width':'petal_width'])

print(df.iloc[-5:,[1,3]])

print(df.loc[df ['sepal_length'] > 6, ['sepal_length','sepal_width']])

