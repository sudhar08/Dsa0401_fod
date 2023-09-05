import pandas as pd
a={'post':["post1","post2","post3","post4"],
   'likes':[1250,1300,1500,1250]}
b=pd.DataFrame(a)
print(b)
c=b['likes'].value_counts()
print("FREQUENCY=",c)
