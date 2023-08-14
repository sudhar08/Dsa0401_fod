import pandas as pd

property_data = pd.read_csv("property_data.csv")

avg_price_by_location = property_data.groupby('location')['listing_price'].mean()

print("Average listing price of properties in each location:")
print(avg_price_by_location)

properties_with_more_than_four_bedrooms = property_data.loc[property_data['bedrooms'] > 4]

print("Number of properties with more than four bedrooms:")
print(len(properties_with_more_than_four_bedrooms))

property_with_largest_area = property_data.loc[property_data['area'] == property_data['area'].max()]

print("Property with the largest area:")
print(property_with_largest_area)
