import os
import shutil
import zipfile


def extract(source_dir, destination_dir):

    # Ensure the destination folder exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.zip'):
            # Construct the full file path
            file_path = os.path.join(source_dir, filename)
            # Open the ZIP file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all the contents into the destination directory
                zip_ref.extractall(destination_dir)

                print(f"Extracted and moved {filename} to {destination_dir}")

    print("All files have been extracted.")


if __name__ == "__main__":

    extract(source_dir="./", destination_dir="./")