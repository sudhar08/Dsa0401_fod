import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature_values = [ 18,22,25,28,32,40,39,30,29,24,23,20]
rainfall_values = [ 22,20,18,17,15,10,9,14,19,23,25,27]

# 1. Python program to create a line plot of the monthly temperature data
plt.figure(figsize=(7,9))  
plt.plot(months, temperature_values, marker='*', color='b', linestyle='-', linewidth=2)
plt.title('Monthly Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=120)  
plt.tight_layout() 
plt.show()


# 2. Python program to create a scatter plot of the monthly rainfall data
plt.figure(figsize=(8, 9))
plt.scatter(months, rainfall_values, color='r', marker='o')
plt.title('Monthly Rainfall Data')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
 
plt.xticks(rotation=120)  
plt.tight_layout() 
plt.show()
