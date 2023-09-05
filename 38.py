import pandas as pd

# Read the dataset from a CSV file (replace 'dataset.csv' with the actual file name)
data = pd.read_csv("C:/Users/mailm/Downloads/dataset.csv")

# Task 1: Calculate the mean temperature for each city
mean_temperatures = data.groupby('City')['Temperature'].mean()

# Task 2: Calculate the standard deviation of temperature for each city
std_temperatures = data.groupby('City')['Temperature'].std()

# Task 3: Determine the city with the highest temperature range
temperature_range = data.groupby('City')['Temperature'].max() - data.groupby('City')['Temperature'].min()
city_with_highest_range = temperature_range.idxmax()

# Task 4: Find the city with the most consistent temperature (lowest standard deviation)
city_with_lowest_std = std_temperatures.idxmin()

# Display the results
print("Mean temperatures for each city:")
print(mean_temperatures)
print("\nStandard deviation of temperatures for each city:")
print(std_temperatures)
print(f"\nThe city with the highest temperature range is: {city_with_highest_range}")
print(f"The city with the most consistent temperature is: {city_with_lowest_std}")
