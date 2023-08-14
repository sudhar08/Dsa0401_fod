import matplotlib.pyplot as plt

def create_line_plot(months, sales):
    plt.figure(figsize=(10, 6))  

    plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')

    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.legend()

    plt.grid(True) 

    plt.xticks(rotation=45) 
    plt.tight_layout()  

    plt.show()


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1200, 900, 1500, 1800, 2000, 2200, 2100, 2400, 2300, 2500, 2800]

create_line_plot(months, sales)
