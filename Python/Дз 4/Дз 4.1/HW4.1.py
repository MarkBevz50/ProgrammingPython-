import os
import shutil
from datetime import datetime
import argparse

def compare_and_copy(dir_path, dir_diff_path):
    # Зчитуємо файли з обох папочок
    dir_files = {f: os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))}
    dir_diff_files = {f: os.path.join(dir_diff_path, f) for f in os.listdir(dir_diff_path) if os.path.isfile(os.path.join(dir_diff_path, f))}

    for file_name, file_path in dir_files.items():
        # Якщо файла нема в DIR_DIFF, залишаємо в DIR
        if file_name not in dir_diff_files:
            print(f"{file_name} does not exist in {dir_diff_path}, keeping it.")
        else:
            dir_file_mod_time = os.path.getmtime(file_path)
            dir_diff_file_mod_time = os.path.getmtime(dir_diff_files[file_name])

            if dir_file_mod_time > dir_diff_file_mod_time:
                print(f"{file_name} is newer in {dir_path}, keeping it.")
            else:
                # Якщо файл в DIR_DIFF новіший, видаляємо його з DIR
                print(f"{file_name} is older or the same, removing from {dir_path}.")
                os.remove(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare and copy files between two directories.")
    parser.add_argument("dir_path", help="Path to the main directory")
    parser.add_argument("dir_diff_path", help="Path to the directory to compare against")

    args = parser.parse_args()

    compare_and_copy(args.dir_path, args.dir_diff_path)
#python HW4.1.py "C:\Users\bevzm\OneDrive\Desktop\Python\Дз 4\Дз 4.1\DIR" "C:\Users\bevzm\OneDrive\Desktop\Python\Дз 4\Дз 4.1\DIR_DIFF"