import os

def GetFilesInFolder(folder_path):
    """
    Get a list of all files in a folder.
    
    Args:
        folder_path (str): The path to the folder.

    Returns:
        List[str]: A list of file names in the folder.
    """
    if not os.path.isdir(folder_path):
        raise ValueError("The provided path is not a valid directory.")
    
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(file)
    
    return file_list