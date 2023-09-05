import pandas as pd
data=pd.read_csv("C:/Users/VSJN/Desktop/fod/redmi6.csv")
print(data)
data2=data['Review Title'].value_counts()
print(data2)



