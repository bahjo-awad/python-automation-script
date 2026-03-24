import os
import shutil

# folder that contains the files
SOURCE_FOLDER = "sample_files"

# file types to sort
FILE_TYPES = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".txt"],
    "Code": [".py", ".js"]
}

def get_folder(filename):
    name, extension = os.path.splitext(filename)
    extension = extension.lower()

    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder

    return "Other"


def organise_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Folder not found")
        return

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            folder_name = get_folder(file)
            target_folder = os.path.join(SOURCE_FOLDER, folder_name)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved {file} to {folder_name}")


if __name__ == "__main__":
    organise_files()
