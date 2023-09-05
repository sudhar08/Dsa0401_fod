import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("F:/mobile_prices.csv")
print(data)
data1=data[data['touch_screen']>0].head(12)
print(data1)
data2=data[data['price_range']>2].head(12)
print(data1)
plt.plot(data1,data2)
plt.show()
