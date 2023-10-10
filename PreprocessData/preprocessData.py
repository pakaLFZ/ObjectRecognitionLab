import json
import csv
from getFilenameList import GetFilesInFolder
from imageVectorize import process_image
from getDataFromCSV import getDataFromCSV
import pandas as pd
table = pd.read_csv("dataset.csv")

imageLocation = "../images/"
imagesList = GetFilesInFolder(imageLocation)


imagesList = imagesList[:5000]

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

    x = process_image(imageLocation+image)
    X.append(x.tolist())

    if id % 500 == 0:
        percentage = (id/len(imagesList)) * 100
        percentage = round(percentage, 2)
        print(f"{id} / {len(imagesList)}  |  {percentage}")

log = open("X.json", "w")
log.write(json.dumps(X))
log.flush()

log = open("Y.json", "w")
log.write(json.dumps(Y))
log.flush()


print("done")
