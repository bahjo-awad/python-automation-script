import os
import shutil

# Folder to organise
SOURCE_FOLDER = "sample_files"

# File type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Code": [".py", ".js", ".html", ".css"],
}


def create_folder_if_missing(folder_path):
    """Create folder if it does not already exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def get_category(filename):
    """Return the category for a file based on its extension."""
    _, extension = os.path.splitext(filename)
    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def organise_files():
    """Move files into category folders."""
    create_folder_if_missing(SOURCE_FOLDER)

    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isfile(file_path):
            category = get_category(filename)
            category_folder = os.path.join(SOURCE_FOLDER, category)

            create_folder_if_missing(category_folder)

            destination_path = os.path.join(category_folder, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved '{filename}' to '{category}/'")


if __name__ == "__main__":
    organise_files()
