import os
import shutil

dd_dir = "/home/rodrigo/Downloads"
pictures_dir = "/home/rodrigo/Pictures"
document_dir = "/home/rodrigo/Documents"
del_dir = "/home/rodrigo/Delete"

files = os.listdir(dd_dir)

for file in files:
    file_path = os.path.join(dd_dir, file)
    
    #Check if file is an image
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.mp3', '.mp4')):
        shutil.move(file_path, pictures_dir)
        print("Moved {file} to {pictures_dir}")
    
    # Check if file is a document
    elif file.lower().endswith(('.pdf', '.doc', '.docx', '.txt')):
        shutil.move(file_path, document_dir)
        print("Moved {file} to {document_dir}")
    
    # Otherwise, move it to the 'delete' directory
    else:
        shutil.move(file_path, del_dir)
        print("Moved {file} to {other_dir}")
