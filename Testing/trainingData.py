import numpy as np
import json
from sklearn.model_selection import train_test_split
from model import Model

X = open("dataPreprocess/X.json", "r").read()
X = json.loads(X)
X = np.array(X)

Y = open("dataPreprocess/Y.json", "r").read()
Y = json.loads(Y)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

model = Model()