import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/VSJN/Desktop/fod/redmi6.csv")
print(data)
data1=np.array(data)
print(data1)
data2=len(data1)
print(data2)
for data1 in range(data2):
    if(data1=="," and data1=="."):
        data3=data1.replace(",","")
    print(data1)
