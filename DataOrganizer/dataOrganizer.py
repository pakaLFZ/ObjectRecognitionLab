import csv, json, random

from getFilenameList import GetFilesInFolder 
from json2csv import json_to_csv


# Define the fields for the dictionary
fields = [
    "filename", 
    "Cardboard", 
    "Glass", 
    "Garbage",
    "Metal", 
    "Paper", 
    "Plastic", 
    "Trash", 
    "GarbageBag",
    "PaperBag",
    "PlasticBag",
    "Null"
]


rubblishList = []
csv_file = 'Garbage_Classifier.v27i.multiclass_train.csv'
with open(csv_file, 'r') as f:
    csv_reader = csv.DictReader(f, fieldnames=fields)
    for row in csv_reader:
        data_dict = row
        data_dict["GarbageBag"] = 0
        data_dict["PaperBag"] = 0
        data_dict["PlasticBag"] = 0
        data_dict["Null"] = 0
        if data_dict["Garbage"] == 1:
            data_dict["Trash"] == 1
        del data_dict["Garbage"]
        rubblishList.append(data_dict)

rubblishList_test = []
csv_file = 'Garbage_Classifier.v27i.multiclass_test.csv'
with open(csv_file, 'r') as f:
    csv_reader = csv.DictReader(f, fieldnames=fields)
    for row in csv_reader:
        data_dict = row
        data_dict["GarbageBag"] = 0
        data_dict["PaperBag"] = 0
        data_dict["PlasticBag"] = 0
        data_dict["Null"] = 0
        if data_dict["Garbage"] == 1:
            data_dict["Trash"] == 1
        del data_dict["Garbage"]
        rubblishList_test.append(data_dict)



garbageBagList = []
garbageBagList_test = []
garbageBagFiles = GetFilesInFolder(r"..Garbage Bags\Bag Classes\Garbage Bag Images")
for filename in garbageBagFiles:
    data_dict = {
        "filename": filename, 
        "Cardboard": 0, 
        "Glass": 0, 
        "Metal": 0, 
        "Paper": 0, 
        "Plastic": 0, 
        "Trash": 0, 
        "GarbageBag": 1,
        "PaperBag": 0,
        "PlasticBag": 0,
        "Null": 0
    }
    garbageBagList.append(data_dict)


paperBagList = []
paperBagList_test = []
paperBagFiles = GetFilesInFolder(r"..\Garbage Bags\Bag Classes\Paper Bag Images")
for filename in paperBagFiles:
    data_dict = {
        "filename": filename, 
        "Cardboard": 0, 
        "Glass": 0, 
        "Metal": 0, 
        "Paper": 0, 
        "Plastic": 0, 
        "Trash": 0, 
        "GarbageBag": 0,
        "PaperBag": 1,
        "PlasticBag": 0,
        "Null": 0
    }
    paperBagList.append(data_dict)


plasticBagList = []
plasticBagList_test = []
plasticBagFiles = GetFilesInFolder(r"..\Garbage Bags\Bag Classes\Plastic Bag Images")
for filename in plasticBagFiles:
    data_dict = {
        "filename": filename, 
        "Cardboard": 0, 
        "Glass": 0, 
        "Metal": 0, 
        "Paper": 0, 
        "Plastic": 0, 
        "Trash": 0, 
        "GarbageBag": 0,
        "PaperBag": 0,
        "PlasticBag": 1,
        "Null": 0
    }
    plasticBagList.append(data_dict)

emptyList = []
emptyFileList = GetFilesInFolder(r"..\Litter Street Images.v10-litterstreettiled.multiclass\empty")
for filename in plasticBagFiles:
    data_dict = {
        "filename": filename, 
        "Cardboard": 0, 
        "Glass": 0, 
        "Metal": 0, 
        "Paper": 0, 
        "Plastic": 0, 
        "Trash": 0, 
        "GarbageBag": 0,
        "PaperBag": 0,
        "PlasticBag": 0,
        "Null": 1
    }
    emptyList.append(data_dict)



dataset = rubblishList + rubblishList_test + garbageBagList + paperBagList + plasticBagList  + emptyList

random.shuffle(dataset)

json_to_csv(dataset, "dataset.csv")
print("done")