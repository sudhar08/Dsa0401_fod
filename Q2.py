import numpy as np  
sales_data = np.array([[100, 200, 150],
                       [50, 120, 180],
                       [80, 90, 100]])

total_sales_per_product = np.sum(sales_data, axis=1)

overall_sum = np.sum(sales_data)

total_products = sales_data.shape[0] * sales_data.shape[1]
average_price = overall_sum / total_products

print(f"The average price of all products sold in the past month is: {average_price}")
