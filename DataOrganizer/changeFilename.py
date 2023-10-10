import os

def changeFilename(location, new_filename):
    try:
        # Split the location into the directory path and the current filename
        directory, current_filename = os.path.split(location)
        
        # Create the new file path by combining the directory and the new filename
        new_location = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(location, new_location)
    except FileNotFoundError:
        print(f"File not found: {location}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")