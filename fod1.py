import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#input data
data=pd.read_csv("C:/Users/VSJN/Desktop/fod/Fod1.csv")
print(data)
data1=np.array(data)
print(data1)

#maths
maths=np.array(data)[:,1]
print(maths)
len1=len(maths)
avg1=sum(maths)/len1
print(avg1)
 #english
eng=np.array(data)[:,2]
print(eng)
avg2=sum(eng)/len(eng)
print(avg2)

#science
sci=np.array(data)[:,3]
print(sci)
avg3=sum(sci)/len(sci)
print(avg3)

#history
his=np.array(data)[:,3]
print(his)
avg4=sum(his)/len(his)
print(avg4)

#printing which has highest avg
if(avg1>avg2 and avg1>avg3 and avg1>avg4):
    print("maths has high avg")
elif(avg2>avg1 and avg2>avg3 and avg2>avg4):
    print("engish has high avg")
elif(avg3>avg1 and avg3>avg2 and avg3>avg4):
    print("science has high avg")
else:
    print("history has high avg")

plt.scatter(maths,eng)
plt.show()
