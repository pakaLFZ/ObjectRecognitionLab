from imageVectorize import process_image
from model import Model
import numpy as np
import json

model = Model()
model.load()

def TestImg(filename="test.jpg"):
    image = process_image("test.jpg", 128)
    score, prediction = model.predict(image)
    print(f"This is a {prediction}", score)

TestImg("test.jpg")
while True:
    filename = input("Enter the name of the image: ")
    try:
        TestImg(filename)
    except:
        print("Something went wrong. Try again.\n")
