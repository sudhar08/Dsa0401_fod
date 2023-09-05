import numpy as np
import matplotlib.pyplot as plt
cost=np.array([10,20,30])
qu=np.array([2,3,2])
dis=10
tax=8
for i in range(len(cost)):
    tot=cost*qu
    tot1=tot-tot*(dis/100)
    tot2=tot1+tot1*(tax/100)
    total=sum(tot2)
    

print("total purchased amount after discount and tax added :",total)
print(tot2)
print(tot1)
plt.plot(cost)
plt.show()
