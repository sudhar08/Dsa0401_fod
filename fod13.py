import pandas as pd
with open("C:/Users/VSJN/Desktop/fod/fod.txt", "r") as file:
    text = file.read()
data=text.split()
data2=pd.DataFrame(data)
data3=data2[0].value_counts()
print(data3)
