import os

def copyFile(source_file, destination_file):
    source_file_ = cleanFilename(source_file)
    try:
        msg = f"copy {source_file_} {destination_file}"
        os.system(msg)
    except FileNotFoundError:
        print("File not found: ", source_file)
    except Exception as e:
        print(f"An error occurred: {str(e)}: ", source_file)


def cleanFilename(name):
    name_ = name
    name_ = name_.split("\\")
    
    location = ""
    for item in range(len(name_) - 1):
        location += f'"{name_[item]}"\\'
    location += name_[-1]
    return location
    

