import pandas as pd

def calculate_age_frequency_distribution(df):
    age_frequency = df['Age'].value_counts().sort_index()
    return age_frequency
def main():
    sales_data = pd.read_csv('your_sales_data.csv')
    age_frequency_distribution = calculate_age_frequency_distribution(sales_data)
    print("Frequency Distribution of Ages:")
    print(age_frequency_distribution)

if _name_ == "_main_":
    main()
