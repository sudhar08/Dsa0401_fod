import matplotlib.pyplot as plt

def create_rainfall_scatter_plot(months, rainfall):
    plt.figure(figsize=(10, 6))  # Optional: Set the figure size (width, height) in inches

    plt.scatter(months, rainfall, color='r', label='Rainfall (mm)')

    plt.title('Monthly Rainfall Data')
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.legend()

    plt.grid(True)  # Optional: Display grid lines

    plt.xticks(rotation=45)  # Optional: Rotate the x-axis labels if they are too long
    plt.tight_layout()  # Optional: Adjusts the spacing of the plot

    plt.show()

# Example data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [50, 60, 70, 80, 100, 120, 150, 140, 130, 100, 80, 60]

create_rainfall_scatter_plot(months, rainfall)
