import pandas as pd
data ={
    "product name " :["lays","kurkure","mad angles","lays","kurkure","mad angles","lays","kurkure","mad angles"],
    "order quantity" :[10,5,20,15,20,30,45,25,10]
    }
sales_data =pd.DataFrame(data)
print(sales_data)
sorted_product = sales_data.sort_values(by="order quantity",ascending=False)
print(sorted_product)
top_5_products = sorted_product.head(5)
print(top_5_products)
