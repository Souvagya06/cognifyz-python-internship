import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    # File type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Others": []
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)

        moved = False

        for category, extensions in file_types.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(folder_path, category)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file))
                moved = True
                break

        if not moved:
            target_folder = os.path.join(folder_path, "Others")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))

    print("Files organized successfully!")


# Input folder path
folder = input("Enter folder path to organize: ")

organize_files(folder)