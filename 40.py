import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file into a pandas data frame
df = pd.read_csv("C:/Users/mailm/Downloads/football_players.csv")

# Find the top 5 players with the highest number of goals scored
top_goals_players = df.nlargest(5, 'Goals')
print("Top 5 Players with the Highest Number of Goals Scored:")
print(top_goals_players[['Player', 'Goals']])

# Find the top 5 players with the highest salaries
top_salary_players = df.nlargest(5, 'Salary')
print("\nTop 5 Players with the Highest Salaries:")
print(top_salary_players[['Player', 'Salary']])

# Calculate the average age of players
average_age = df['Age'].mean()
print("\nAverage Age of Players:", average_age)

# Display the names of players who are above the average age
above_average_age_players = df[df['Age'] > average_age]
print("\nPlayers Above the Average Age:")
print(above_average_age_players[['Player', 'Age']])

# Visualize the distribution of players based on their positions using a bar chart
position_counts = df['Position'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(position_counts.index, position_counts.values)
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.title('Distribution of Players Based on Positions')
plt.xticks(rotation=45)
plt.show()
