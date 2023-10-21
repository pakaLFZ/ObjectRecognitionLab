print(">>> Loading imported modules.")
from model import Model
from confusionMatrix import confusionMatrix
import numpy as np
import json

print(">>> Loading models.")
model = Model()
model.load()

matrix = confusionMatrix([
    "GarbageBag",
    "PlasticBag",
    "PaperBag",
    "Null"
])

print(">>> Loading testing data.")
X = open("X_0.pickle", "r").read()
X = json.loads(X)

Y = open("Y_0.pickle", "r").read()
Y = json.loads(Y)

for i in range(len(X)):
    if i % 100 == 0:
        msg = f"Processing {i}/{len(X)}"
        print(msg)
    x = X[i]
    y = Y[i]
    scores, prediction = model.predict(x)
    matrix.load(scores, y)

print(matrix.matrix)



