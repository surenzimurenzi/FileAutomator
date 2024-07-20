import os
import shutil

def create_folders(destination):

    folders = ['Images', 'Videos', 'Audio', 'Documents', 'Archive']
    for folder in folders:
        folder_path = os.path.join(destination, folder)
        os.makedirs(folder_path, exist_ok=True)

def sort_files(destination):
    # Get all files in the destination folder
    files = os.listdir(destination)

    # Sort files into respective folders
    for file in files:
        file_path = os.path.join(destination, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                shutil.move(file_path, os.path.join(destination, 'images'))
            elif file_extension in ['.mp4', '.avi', '.mov', '.wmv']:
                shutil.move(file_path, os.path.join(destination, 'videos'))
            elif file_extension in ['.mp3', '.wav', '.ogg']:
                shutil.move(file_path, os.path.join(destination, 'audio'))
            elif file_extension in ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.pptx']:
                shutil.move(file_path, os.path.join(destination, 'documents'))
            elif file_extension in ['.rar', '.zip']:
                shutil.move(file_path, os.path.join(destination, 'archive'))
            else:
                print(f"Unknown file type: {file}. Skipping...")

def main():
    destination = input("Enter the folder destination: ")
    create_folders(destination)
    sort_files(destination)
    print("Folders created and files sorted successfully!")

if __name__ == "__main__":
    main()