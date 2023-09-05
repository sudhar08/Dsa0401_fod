import pandas as pd
course={ 'sub':['python','cplusplus','python','c','cpluscplus','fod','fod','c']
         ,'coursecount':[34,40,32,40,35,40,34,32]}
data=pd.DataFrame(course)
print(data)
data1=data['coursecount'].value_counts()
print("frequency of the given data :",data1)
