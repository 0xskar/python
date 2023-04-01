import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data and sort by date
data = pd.read_csv('steam_data.csv')
data['Month'] = pd.to_datetime(data['Month'], format='%B %Y')
data = data.sort_values('Month')

# Extract input and output data
X = np.array(data['Month'].apply(lambda x: x.value)).reshape(-1, 1)
y = np.array(data['Average Players']).reshape(-1, 1)

# Normalize the input features
X_norm = (X - np.mean(X)) / np.std(X)
X_norm = np.hstack((np.ones((len(y), 1)), X_norm))

# Initialize fitting parameters
theta = np.zeros((2, 1))

# Set hyperparameters
alpha = 0.01
num_iters = 1500

# Define cost function
def compute_cost(X, y, theta):
    m = len(y)
    h = X @ theta
    J = 1 / (2 * m) * np.sum((h - y) ** 2)
    return J

# Define gradient descent function
def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros((num_iters, 1))
    for i in range(num_iters):
        h = X @ theta
        theta = theta - alpha / m * (X.T @ (h - y))
        J_history[i] = compute_cost(X, y, theta)
    return theta, J_history

# Run gradient descent to get optimal parameters
theta, J_history = gradient_descent(X_norm, y, theta, alpha, num_iters)

# Plot data and predictions
plt.plot(data['Month'], y, 'bo', label='Data')
plt.plot(data['Month'], X_norm @ theta, 'r-', label='Prediction')
plt.xlabel('Month')
plt.ylabel('Average Players')
plt.title('ESO Player Retention')
plt.legend()
plt.show()

# Predict next month's player base
next_month = pd.to_datetime('April 2023', format='%B %Y').value
next_month_norm = (next_month - np.mean(X)) / np.std(X)
next_month_norm = np.hstack((1, next_month_norm))
next_month_players = next_month_norm @ theta
print(f'Next month\'s player base is predicted to be {next_month_players[0]:.2f}')
