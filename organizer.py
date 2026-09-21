import os
import shutil

# Define the folder you want to organize
# For testing, create a folder called "TestFolder" on your desktop and put some random files in it
FOLDER_TO_ORGANIZE = "TestFolder"

# Define how you want to sort your files
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"]
}

def organize_folder():
    if not os.path.exists(FOLDER_TO_ORGANIZE):
        print(f"Error: The folder '{FOLDER_TO_ORGANIZE}' does not exist.")
        return

    # Go through every file in the folder
    for filename in os.listdir(FOLDER_TO_ORGANIZE):
        file_path = os.path.join(FOLDER_TO_ORGANIZE, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        moved = False
        # Check which category the file belongs to
        for category, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                # Create the category folder if it doesn't exist
                category_folder = os.path.join(FOLDER_TO_ORGANIZE, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                
                # Move the file
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category}")
                moved = True
                break
        
        if not moved:
            print(f"Skipped {filename} (Unknown file type)")

if __name__ == "__main__":
    print("Starting file organization...")
    organize_folder()
    print("Organization complete!")
