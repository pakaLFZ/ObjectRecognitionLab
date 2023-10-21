import csv, json, random

from getFilenameList import GetFilesInFolder, ListEveryFile
from json2csv import json_to_csv
from copyFile import copyFile
import numpy as np


# Define the fields for the dictionary
fields = [
    "filename", 
    "Garbage",
    "Null"
]

sourceFolder = r"D:\0Business\ML\Hackathon\ObjectRecognitionLab\img"

garbageBagList = []
garbageBagList_test = []
folder = r"D:\0Business\ML\Hackathon\sources\GarbageBags\BagClasses\GarbageBagImages"
garbageBagFiles = GetFilesInFolder(folder)
for filename in garbageBagFiles:
    fileLocation = folder + "\\" + filename
    destinationLocation = sourceFolder + "\\" + filename
    # copyFile(fileLocation, destinationLocation)

    data_dict = {
        "filename": filename, 
        "GarbageBag": 1,
        "PlasticBag": 0,
        "PaperBag": 0,
        "Null": 0
    }
    garbageBagList.append(data_dict)

plasticBagList = []
folder = r"D:\0Business\ML\Hackathon\sources\GarbageBags\BagClasses\Plastic Bag Images"
garbageBagFiles = GetFilesInFolder(folder)
for filename in garbageBagFiles:
    fileLocation = folder + "\\" + filename
    destinationLocation = sourceFolder + "\\" + filename
    # copyFile(fileLocation, destinationLocation)

    data_dict = {
        "filename": filename, 
        "GarbageBag": 0,
        "PlasticBag": 1,
        "PaperBag": 0,
        "Null": 0
    }
    plasticBagList.append(data_dict)

paperBagList = []
folder = r"D:\0Business\ML\Hackathon\sources\GarbageBags\BagClasses\Paper Bag Images"
garbageBagFiles = GetFilesInFolder(folder)
for filename in garbageBagFiles:
    fileLocation = folder + "\\" + filename
    destinationLocation = sourceFolder + "\\" + filename
    # copyFile(fileLocation, destinationLocation)

    data_dict = {
        "filename": filename, 
        "GarbageBag": 0,
        "PlasticBag": 0,
        "PaperBag": 1,
        "Null": 0
    }
    paperBagList.append(data_dict)


emptyList = []
folder = r"D:\0Business\ML\Hackathon\sources\not_trash"
# folder = r"D:\0Business\ML\Hackathon\sources\GarbageClassifier.v27i.multiclass\train"
emptyFileList = ListEveryFile(folder)
for filePath, filename in emptyFileList:
    fileLocation = filePath
    destinationLocation = sourceFolder + "\\" + filename
    copyFile(fileLocation, destinationLocation)

    data_dict = {
        "filename": filename, 
        "GarbageBag": 0,
        "PlasticBag": 0,
        "PaperBag": 0,
        "Null": 1
    }
    emptyList.append(data_dict)


sampleSize = np.array([
    len(garbageBagList),
    len(plasticBagList),
    len(paperBagList),
    len(emptyList),
])
sampleSize = np.min(sampleSize)

dataList = garbageBagList[:sampleSize] + plasticBagList[: sampleSize] + paperBagList[: sampleSize] + emptyList[: sampleSize]
random.shuffle(dataList)

json_to_csv(dataList, "dataset.csv")
print("done")