import csv, json, random

from getFilenameList import GetFilesInFolder, ListEveryFile
from json2csv import json_to_csv
from copyFile import copyFile



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
        "Garbage": 1,
        "Null": 0
    }
    garbageBagList.append(data_dict)
print("garbageBagList: ", len(garbageBagList))


emptyList = []
# folder = r"D:\0Business\ML\Hackathon\sources\not_trash"
folder = r"D:\0Business\ML\Hackathon\sources\GarbageClassifier.v27i.multiclass\train"
emptyFileList = ListEveryFile(folder)
for filePath, filename in emptyFileList:
    fileLocation = filePath
    destinationLocation = sourceFolder + "\\" + filename
    # copyFile(fileLocation, destinationLocation)

    data_dict = {
        "filename": filename, 
        "Garbage": 0,
        "Null": 1
    }
    emptyList.append(data_dict)

garbageBagList = garbageBagList[:len(emptyList)]
print("emptyList: ", len(emptyList))
random.shuffle(emptyList)

dataset =  garbageBagList + emptyList
random.shuffle(dataset)

json_to_csv(dataset, "dataset.csv")
print("done")