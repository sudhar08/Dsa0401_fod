from sklearn.linear_model import LinearRegression
dataset = [
    [1500, 3, 1, 250000],
    [2000, 4, 2, 350000],
    [1200, 2, 1, 180000],
    [1800, 3, 3, 280000],
]
X = [[house[0], house[1], house[2]] for house in dataset]
y = [house[3] for house in dataset]
model = LinearRegression()
model.fit(X, y)
def get_new_house_input():
    area = float(input("Enter area (sq. ft.): "))
    bedrooms = int(input("Enter number of bedrooms: "))
    location = int(input("Enter location (e.g., 1 for city center, 2 for suburbs, etc.): "))
    return [area, bedrooms, location]
new_house = get_new_house_input()
predicted_price = model.predict([new_house])
print(f"The predicted price of the new house is: ${predicted_price[0]:.2f}")
