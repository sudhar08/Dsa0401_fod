import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1=pd.read_csv("C:/Users/VSJN/Desktop/fod/sales_data_sample.csv")
print(data1)
data2=np.array(data1)[:,0]
print(data2)
avg1=sum(data2)/len(data2)
print(avg1)
