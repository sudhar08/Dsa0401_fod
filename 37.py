import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data for study time and exam scores
np.random.seed(42)  # For reproducibility
num_students = 100
study_time = np.random.randint(1, 10, num_students)
exam_scores = np.random.randint(50, 100, num_students)

# Create a DataFrame to store the data
data = pd.DataFrame({'Study Time (hours)': study_time, 'Exam Scores': exam_scores})

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['Study Time (hours)'], data['Exam Scores'])
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Scores')
plt.title('Study Time vs. Exam Scores')
plt.show()

# Line plot
plt.figure(figsize=(8, 6))
plt.plot(data['Study Time (hours)'], data['Exam Scores'], marker='o')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Scores')
plt.title('Study Time vs. Exam Scores')
plt.show()

# Correlation coefficient
correlation_coeff = data['Study Time (hours)'].corr(data['Exam Scores'])
print(f"Correlation Coefficient: {correlation_coeff}")
