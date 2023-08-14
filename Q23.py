import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import csv  

def perform_hypothesis_test(control_data, treatment_data, alpha):
    _, p_value = stats.ttest_ind(control_data, treatment_data)
    return p_value < alpha

with open("names.csv", mode="w", newline='') as csvfile:
    fieldnames = ["Group", "Value"]  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Group": "Control", "Value": 10.2})  
    writer.writerow({"Group": "Control", "Value": 9.8})  
    writer.writerow({"Group": "Treatment", "Value": 12.1}) 
    writer.writerow({"Group": "Treatment", "Value": 11.4})  
    

if _name_ == "_main_":
    file_name = input("Enter the CSV file name containing clinical trial data: ")

    data = pd.read_csv(file_name)

    control_data = data[data["Group"] == "Control"]["Value"]
    treatment_data = data[data["Group"] == "Treatment"]["Value"]

    alpha = float(input("Enter the significance level (alpha) for the hypothesis test: "))

    is_significant = perform_hypothesis_test(control_data, treatment_data, alpha)

    plt.figure(figsize=(8, 6))
    plt.hist(control_data, bins=10, alpha=0.5, label="Control Group")
    plt.hist(treatment_data, bins=10, alpha=0.5, label="Treatment Group")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Clinical Trial Data")
    plt.legend()

    text = "Statistically Significant" if is_significant else "Not Statistically Significant"
    plt.text(0.5, 0.9, f"Hypothesis Test Result: {text}", ha='center', va='center', transform=plt.gca().transAxes)

    plt.show()
