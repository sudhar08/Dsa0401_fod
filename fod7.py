import pandas as pd
data = {
    'customerid': [11, 12, 13, 11, 14, 15, 13],
    'productid': [1, 2, 1, 3, 2, 1, 3],
    'orderdate': ['2022-06-01', '2022-06-02', '2022-06-03', '2022-06-04', '2022-06-05', '2022-06-06', '2022-06-07'],
    'orderquantity': [5, 10, 7, 3, 8, 6, 4]
}

dat1= pd.DataFrame(data)
count1= dat1.groupby('customerid')['orderdate']
count2=count1.count()
print("Total Number of Orders by the Customer:")
print(count2)
avg=dat1.groupby('productid')['orderquantity']
avg1=avg.mean()
print("Average of  Each Product:")
print(avg1)
ear=dat1['orderdate'].min()
lat=dat1['orderdate'].max()
print("earlier date:",ear)
print("latest date:",lat)
