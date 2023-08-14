import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats  
data = {
    'age': [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61],
    'fat_percentage': [9.2,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]
}
df = pd.DataFrame(data)
age_mean = df['age'].mean()
age_median = df['age'].median()
age_std = df['age'].std()
fat_mean = df['fat_percentage'].mean()
fat_median = df['fat_percentage'].median()
fat_std = df['fat_percentage'].std()
print(f"Age Mean: {age_mean}")
print(f"Age Median: {age_median}")
print(f"Age Standard Deviation: {age_std}")
print(f"%Fat Mean: {fat_mean}")
print(f"%Fat Median: {fat_median}")
print(f"%Fat Standard Deviation: {fat_std}")
plt.figure(figsize=(8, 6))
df.boxplot(column=['age', 'fat_percentage'])
plt.title("Boxplots for Age and %Fat")
plt.ylabel("Values")
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['fat_percentage'])
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.title("Scatter Plot of Age vs %Fat")
plt.show()
plt.figure(figsize=(10, 6))
stats.probplot(df['age'], plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()
plt.figure(figsize=(10, 6))
stats.probplot(df['fat_percentage'], plot=plt)
plt.title("Q-Q Plot of %Fat")
plt.show()
