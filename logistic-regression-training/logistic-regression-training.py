import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    w = np.zeros(X.shape[1])
    b = 0
    N =  X.shape[0]

    for i in range(steps):
        z = np.dot(X, w) + b
        p = _sigmoid(z)

        # Update Gradients
        dw = (1/N) * np.dot(X.T, (p - y))
        db = (1/N) * np.sum(p - y)
        
        # update w and b
        w = w - (lr * dw)
        b = b - (lr * db)

    return (w, b)