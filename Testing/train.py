print(">>> Start loading modules.")
import numpy as np
import json, pickle
from sklearn.model_selection import train_test_split
from model import Model

model = Model()
print(">>> Start training processes.")
X_combined = []
Y_combined = []

sampleSize = 10
for i in range(sampleSize):
    print(f"...Performing {i} / {sampleSize}")
    X = open(f"../PreprocessData/data/X_{i}.pickle", "r").read()
    X = json.loads(X)

    Y = open(f"../PreprocessData/data/Y_{i}.pickle", "r").read()
    Y = json.loads(Y)

    X_combined += X
    Y_combined += Y
X = []
Y = []


X_combined= np.array(X_combined)
Y_combined= np.array(Y_combined)

X_train, X_test, Y_train, Y_test = train_test_split(X_combined, Y_combined, test_size=0.1, random_state=0)

X_combined = []
Y_combined = []

model.train(X_train, Y_train, X_test, Y_test, 3)
model.save()