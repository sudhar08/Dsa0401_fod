import numpy as np
import pandas as pd
def calculate_confidence_interval(sample_size, confidence_level, standard_error):
    critical_value = 1.96 
    margin_of_error = critical_value * standard_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound
def main():
    filename = "rare_elements.csv"
    data = pd.read_csv(filename)
    sample_size = int(input("Enter the sample size: "))
    confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
    desired_precision = float(input("Enter the desired level of precision: "))
    sample = np.random.choice(data['concentration'], size=sample_size, replace=False)
    sample_mean = np.mean(sample)
    standard_error = np.std(sample, ddof=1) / np.sqrt(sample_size)
    lower_bound, upper_bound = calculate_confidence_interval(sample_size, confidence_level, standard_error)
    required_sample_size = ((1.96 * standard_error) / desired_precision)**2
    print(f"\nSample Mean: {sample_mean}")
    print(f"Confidence Interval ({confidence_level * 100}%): ({lower_bound}, {upper_bound})")
    print(f"Required Sample Size for Desired Precision: {required_sample_size:.2f}")
if __name__ == "__main__":
    main()
