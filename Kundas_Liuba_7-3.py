import os
import shutil

path_file = r'my_project\authapp\templates\authapp'
dest_file = r'my_project\mainapp\templates'

if os.path.exists(path_file):
    shutil.move(path_file, dest_file)


