import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'number_of_bedrooms': [3, 4, 5, 2, 6],
    'area_sqft': [1500, 1800, 2200, 1200, 2500],
    'listing_price': [250000, 300000, 350000, 200000, 400000]
}
data1= pd.DataFrame(data)
avg=data1.groupby('location')['listing_price'].mean()
bed1= data1[data1['number_of_bedrooms'] > 4]
bed2=len(bed1)
area=data1[data1['area_sqft']==data1['area_sqft'].max()]
print(avg)
print("Number of properties with more than four bedrooms:")
print(bed2)
print("Property with the largest area:")
print(area)
