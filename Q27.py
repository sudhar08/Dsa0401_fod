from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
dataset = [
    [200, 12, 1, 0],   
    [100, 6, 2, 1],    
    [300, 24, 3, 0],   
    [150, 18, 1, 1],   
]
X = [[customer[0], customer[1], customer[2]] for customer in dataset]
y = [customer[3] for customer in dataset]
model = LogisticRegression()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model.fit(X_scaled, y)
def get_new_customer_input():
    usage_minutes = float(input("Enter usage minutes: "))
    contract_duration = int(input("Enter contract duration (months): "))
    demographic_data = int(input("Enter demographic data (e.g., 1 for young, 2 for middle-aged, 3 for elderly): "))
    return [usage_minutes, contract_duration, demographic_data]
new_customer = get_new_customer_input()
new_customer_scaled = scaler.transform([new_customer])
predicted_churn_status = model.predict(new_customer_scaled)
if predicted_churn_status[0] == 0:
    print("The model predicts that the customer will not churn.")
else:
    print("The model predicts that the customer will churn.")
