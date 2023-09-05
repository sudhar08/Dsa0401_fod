import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_values = [1000, 1200, 800, 1500, 1400, 1600, 1100, 1300, 1700, 1900, 2000, 1800]

# Create a line plot
plt.figure(figsize=(8, 6))  # Set the figure size
plt.plot(months, sales_values, marker='.', color='b', linestyle='-', linewidth=2,ms=5.0)
plt.title('Product Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)  # Show gridlines
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()

# Create a bar plot
plt.figure(figsize=(8, 6)) 
plt.bar(months, sales_values, color='g')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()

# Create a scatter plot
plt.figure(figsize=(8, 6))  
plt.scatter(months, sales_values, color='r', marker='o')
plt.title('Product Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True) 
plt.xticks(rotation=45) 
plt.tight_layout()  
plt.show()
