import os

dir_name_main = "my_project"
if not os.path.exists(dir_name_main):
    os.mkdir(dir_name_main)

my_project = ("settings", "mainapp", "adminap", "authapp")
#settings = ("__init__.py", "dev.py", "prod.py")

[os.makedirs(os.path.join(dir_name_main, i)) for i in my_project if not os.path.exists(i)]
