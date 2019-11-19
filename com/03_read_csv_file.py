import pandas as pd
import numpy as np
# df : dataframe is the table
df = pd.read_csv("./data/Results.csv") # Read csv file(Results.csv) under the the "data" folder
print(df.tail(2))

# List_temp=[1, 2, 3]
# s1=pd.core.series.Series([1,2,3])
# s2=pd.core.series.Series(["one","two","three"])
# print(pd.DataFrame( data= dict( num=s1, word =s2)) )

df = pd.DataFrame({"a" : [4 ,5, 6],"b" : [7, 8, 9],"c" : [10, 11, 12]},index = [1, 2, 3])
print(df)
print()
print(df["c"])
print(df[["a","c"]])

print(df.loc[1])
print(df.loc[3, "a"])
print(df.loc[[1,3], ["a", "b"]])

df = pd.DataFrame ([[4, 7, 10], [5, 8, 11], [6, 9, 12]], index=[1,2,3], columns=['a', 'b', 'c'])

df = pd.DataFrame ({"a" : [4 ,5, 6, 6, np.nan], "b" : [7, 8, np.nan, 9, 9], "c" : [10, 11, 12, np.nan, 12]},
                    index = pd.MultiIndex.from_tuples([('d',1),('d',2),('e',2),('e',3),('e',4)],
                    names=['n','v']))

print(df)
print(df[df.a == 5])
print(df[df.b > 7])
print(df[df['b'] > 7])


print(df)
df=df.drop_duplicates(keep='last')
print(df)

print()
print(df[df["b"] !=7])

print(df.a.isin([ 5]))
print(df["a"].isin([6]))     # When the column name is Korean :


print(pd.isnull(df))
print(df['a'].isnull().sum())

print(pd.notnull(df))
print(df.notnull().sum())
print(df["a"].notnull().sum())

print(df.a.notnull())

print(df[df.b == 7 ] & df[df.a == 5])


df[['width','length','species']]
