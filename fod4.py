import numpy as np
data=np.array([1200,24000,3000,5698])
print(data)
fourth=(data[3]-data[0])/100
print("fourth quater total percentage : \n",fourth)
diff=(fourth/data[0])*100
print("percentage increased from first to fourth quater :",round(diff,2))
