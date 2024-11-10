import os
import shutil


def declutter(folder_path, move_files=True):
    file_types = {}
    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)):
            ext = item.split('.')[-1]
            if ext not in file_types:
                file_types[ext] = []
            file_types[ext].append(item)
    for ext, items in file_types.items():
        ext_folder = os.path.join(folder_path, ext.upper() + '_FILES')
        os.makedirs(ext_folder, exist_ok=True)
        for item in items:
            if move_files:
                shutil.move(os.path.join(folder_path, item), os.path.join(ext_folder, item))
            else:
                shutil.copy(os.path.join(folder_path, item), os.path.join(ext_folder, item))

if __name__ == "__main__":
    declutter('/path/to/your/desktop', move_files=True)

