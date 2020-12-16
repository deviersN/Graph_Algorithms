import pandas as pd 

#filename = '../dataset/data.csv'
filename = '../dataset/meteorite-landings.csv'
data = pd.read_csv(filename)
print(data.head())
