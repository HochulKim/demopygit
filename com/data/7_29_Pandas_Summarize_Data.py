import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
print(df.shape)
print()

print(df.head())
print()
print( df['species'].value_counts())   # useful for Category Count rather than number data
print()
pd.DataFrame()
print( pd.DataFrame(df['species'].value_counts()) )  # DataFrame 형태로 보여질
print()
print(len(df))

print(df.shape[0])   # len(df) == df.shape[0] --- True

print(df['sepal_width'].nunique())
print(df.describe())                 # Only Show the rusult for the numerical data not Categorical data
print(df.describe(include =[np.object]))