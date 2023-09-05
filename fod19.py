import pandas as pd
data={'drugs':[10,87,89,65,45,67,84,34,56,75],
'placebo':[12,65,76,44,67,99,65,32,45,65]}
b=pd.DataFrame(data)
print(b)

#drugs
len1=len(b['drugs'])
samplemean=b['drugs'].mean()
st=b['drugs'].std()
standarderror=st/len1
cof=samplemean+(standarderror*1.96)
cof1=samplemean-(standarderror*1.96)

#placebo
print("confidence interval of drugs:",cof,"|",cof1)
len2=len(b['placebo'])
samplemean1=b['placebo'].mean()
st1=b['placebo'].std()
standarderror1=st1/len2
cof2=samplemean1+(standarderror1*1.96)
cof3=samplemean1-(standarderror1*1.96)
print("confidence interval of placebo:",cof2,"|",cof3)

        
