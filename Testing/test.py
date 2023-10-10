from imageVectorize import process_image
from model import Model
import numpy as np
import json

model = Model()
model.load()

def TestImg(filename="test.jpg"):
    image = process_image("test.jpg")
    score, prediction = model.predict(image)
    print(f"This is a {prediction}")

TestImg("test.jpg")