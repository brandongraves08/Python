#Simple Python script to find all files across directors and move them to one directory.

import os
import shutil

# Set your source and destination directories
source_directory = '/path/to/source'
destination_directory = '/path/to/destination'

def move_files_recursively(src, dest):
    # Walk through all directories and files in the source directory
    for root, dirs, files in os.walk(src):
        for file in files:
            # Construct the full path to the file
            file_path = os.path.join(root, file)
            
            # Construct the full path where the file will be moved
            # This just takes the filename and appends it to the destination directory
            dest_path = os.path.join(dest, file)

            # Check if a file with the same name already exists in the destination
            if os.path.isfile(dest_path):
                # If it does, append a number to the filename to avoid overwriting
                basename, extension = os.path.splitext(dest_path)
                counter = 1
                while os.path.isfile(dest_path):
                    dest_path = f"{basename}_{counter}{extension}"
                    counter += 1

            # Move the file
            shutil.move(file_path, dest_path)
            print(f"Moved: {file_path} to {dest_path}")

# Start the moving process
move_files_recursively(source_directory, destination_directory)

print("All files have been moved successfully!")
