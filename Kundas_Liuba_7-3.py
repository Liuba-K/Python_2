import os
import shutil

try:
    for root, dirs, files in os.walk("my_project"):
        if "templates" in dirs:
            for i in os.listdir(os.path.join(root, 'templates')):
                shutil.copytree(os.path.join(root, 'templates', i),
                                os.path.join("my_project", 'templates', i))

except FileExistsError:
    print("Already created templates")
