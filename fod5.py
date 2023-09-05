import numpy as np
car1=np.array([30,45,67,34,54,67,89,20])
car2=np.array([56,67,34,23,45,67,45,23])
avg1=sum(car1)/len(car1)
avg2=sum(car2)/len(car2)
print("average of car model1:",avg1)
print("\n average of car model1:",avg2)
print("\n average increased from model 1 & 2:",(avg1-avg2))
