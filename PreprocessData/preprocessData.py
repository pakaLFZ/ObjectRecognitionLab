import json, pickle
import csv
from getFilenameList import GetFilesInFolder
from imageVectorize import process_image
from getDataFromCSV import getDataFromCSV
from splitList import splitList
import random
import pandas as pd
table = pd.read_csv("dataset.csv")

imageLocation = "../img/"
imagesList_main = GetFilesInFolder(imageLocation)
random.shuffle(imagesList_main)


filenames = table.iloc[:, 0].tolist()
imagesList_main = splitList(filenames, 100)

dataId = 0
for batchNo in range(20):
    print(f"Processing batch {batchNo} ({len(imagesList_main)} batches in total)")
    imagesList = imagesList_main[batchNo]
    X = []
    Y = []
    for id in range(len(imagesList)):
        image = imagesList[id]
        if image.find(".jpg") == -1:
            continue   

        y = getDataFromCSV(table, image)
        if not y:
            continue
        y = [float(i) for i in y]
        Y.append(y)

        x = process_image(imageLocation+image, 128)
        X.append(x.tolist())

        if id % 50 == 0:
            percentage = (id/len(imagesList)) * 100
            percentage = round(percentage, 2)
            print(f"{id} / {len(imagesList)}  |  {percentage}")
    

    log = open(f"data/X_{dataId}.pickle", "w")
    log.write(json.dumps(X))
    log.flush()
    log.close()

    log = open(f"data/Y_{dataId}.pickle", "w")
    log.write(json.dumps(Y))
    log.flush()
    log.close()


    dataId += 1


print("done")
