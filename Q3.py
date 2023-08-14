import numpy as np

house_data = np.array([
    [4, 2000, 250000],
    [5, 2400, 300000],
    [3, 1800, 200000],
    [5, 2800, 350000],
])
bedrooms_greater_than_four = house_data[house_data[:, 0] > 4]
sale_prices = bedrooms_greater_than_four[:, 2]
average_sale_price = np.mean(sale_prices)
print(f"The average sale price of houses with more than four bedrooms is: {average_sale_price}")
