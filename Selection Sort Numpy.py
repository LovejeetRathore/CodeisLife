import numpy as np
def selection(data):
    swap = 0
    for i in range(len(data)):
        swap = i + np.argmin(data[i:])
        (data[i], data[swap]) = (data[swap], data[i])
    return data
X = np.random.randint(50,size=10)
print(X,"\n")
y = selection(X)
print(y)