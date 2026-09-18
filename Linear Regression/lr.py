import numpy as np

X = np.array([
            [10,10],
            [9,8],
            [11,10],
            [2,3],
            [1,1],
            [4,3]
            ],dtype=float)
y = np.array([90,85,95,20,10,30],dtype=float)
m = len(X) # no of samples
n = len(X[0]) # no of features per sample
W = np.zeros(n)
b = 0

def loss(predicted, actual):
    return 0.5 * ((predicted - actual)**2)

def predict(X):
    global W,b
    return np.dot(X,W) + b

def train():
    learning_rate = 0.01
    iterations = 1000
    global W,b
    print("Training...")
    for _ in range(iterations):
        sample_details_printed = False
        for i in range(m):
            p = predict(X[i])
            W -= learning_rate * (p - y[i]) * X[i]
            b -= learning_rate * (p - y[i])
            if _ % 100 == 0 and not sample_details_printed:
                sample_details_printed = True
                print(f"Iteration {_}, Weight: {W}, Bias: {b}, Loss: {loss(p,y[i])}")

train()
new_sample = np.array([5,6])
print(f"Prediction for {new_sample} = {predict(new_sample)}")
