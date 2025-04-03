import numpy as np

def M_C(X, Y):
    X = np.array(X)
    Y = np.array(Y).reshape(-1, 1)
    X_design = np.c_[np.ones(X.shape[0]), X]
    XtX = np.dot(X_design.T, X_design)
    XtX_inv = np.linalg.inv(XtX)
    XtY = np.dot(X_design.T, Y)
    beta = np.dot(XtX_inv, XtY)
    return beta.flatten()

def predict(X, beta):
    X = np.array(X)
    X_design = np.c_[np.ones(X.shape[0]), X]
    return np.dot(X_design, beta)

def MSE(y_true, y_pre):
    return np.mean((np.array(y_true) - np.array(y_pre)) ** 2)

def R2(y_true, y_pre):
    y_true = np.array(y_true)
    y_pre = np.array(y_pre)
    mean_y = np.mean(y_true)
    denominator = np.sum((y_true - mean_y) ** 2)
    numerator = np.sum((y_true - y_pre) ** 2)
    return 1 - (numerator / denominator)

def main():
    n = int(input("Enter number of data points: "))
    m = int(input("Enter number of independent variables: "))
    
    X = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(float(input(f"Enter x[{i+1}][{j+1}]: ")))
        X.append(row)

    Y = []
    for i in range(n):
        Y.append(float(input(f"Enter y[{i+1}]: ")))

    beta = M_C(X, Y)
    y_pre = predict(X, beta)
    mse = MSE(Y, y_pre)
    r2 = R2(Y, y_pre)
    
    print("\n--- Linear Regression Results ---")
    print(f"Coefficients (β): {beta}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R-squared (R²): {r2}")

if _name_ == "_main_":
    main()