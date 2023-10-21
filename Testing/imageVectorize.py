from PIL import Image
import numpy as np

def process_image(filename, size=128):
    # Open the image file
    img = Image.open(filename)
    
    # Resize the image to 64x64
    img = img.resize((size, size))
    
    # Convert the image to a 64x64x3 matrix
    img_matrix = np.array(img)
    
    # Normalize the matrix to values between 0 and 1
    img_matrix = img_matrix / 255.0
    
    # Return the normalized matrix
    return img_matrix
