import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/VSJN/Desktop/fod/Housing.csv")
print(data)
bed=data[data['bedrooms']==4]
print(bed)
bed1=np.array (bed)[:,0]
print(bed1)
avg=sum(bed1)/len(bed1)
print("average price of 4 Bedrooms is : ",round(avg,2))
