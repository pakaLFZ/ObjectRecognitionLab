print(">>> Start loading modules.")
import numpy as np
import json, pickle
from sklearn.model_selection import train_test_split
from model import Model

model = Model()
print(">>> Start training processes.")
X_combined = []
Y_combined = []

now = 1
end = 168

now_batch = 1
batch = 10

X_test = open(f"../PreprocessData/data/X_0.pickle", "r").read()
X_test = json.loads(X_test)

Y_test = open(f"../PreprocessData/data/Y_0.pickle", "r").read()
Y_test = json.loads(Y_test)


while now <= end:
    while now < now_batch + batch:
        print(f"{now} / {now_batch + batch} -- {end}")
        X = open(f"../PreprocessData/data/X_{now}.pickle", "r").read()
        X = json.loads(X)

        Y = open(f"../PreprocessData/data/Y_{now}.pickle", "r").read()
        Y = json.loads(Y)

        X_combined += X
        Y_combined += Y
        now += 1
    X = []
    Y = []

    X_train= np.array(X_combined)
    Y_train= np.array(Y_combined)

    # X_train, X_test, Y_train, Y_test = train_test_split(X_combined, Y_combined, test_size=0.1, random_state=0)

    model.train(X_train, Y_train, X_test, Y_test, 3)
    model.save()

    now_batch = now
