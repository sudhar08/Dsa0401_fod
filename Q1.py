import numpy as np
student_scores = np.array([
    [85, 78, 92, 88],
    [90, 85, 76, 79],
    [78, 92, 88, 82],
])
average_scores = np.mean(student_scores, axis=0)
highest_average_subject_index = np.argmax(average_scores)
subjects = ['Math', 'Science', 'English', 'History']
highest_average_subject = subjects[highest_average_subject_index]

print(f"The average scores for each subject are: {average_scores}")
print(f"The subject with the highest average score is: {highest_average_subject}")
