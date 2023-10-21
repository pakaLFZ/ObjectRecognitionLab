import os

# Get the current working directory
current_directory = os.getcwd()

# Loop through all files in the current directory
for filename in os.listdir(current_directory):
    # Check if the item is a file (not a directory)
    if os.path.isfile(filename):
        # Add "A" to the beginning of the filename
        new_filename = "PL" + filename

        # Rename the file
        os.rename(filename, new_filename)

        # Print a message to indicate the renaming
        print(f'Renamed "{filename}" to "{new_filename}"')
