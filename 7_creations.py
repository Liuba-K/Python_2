#---------------сырой файл
import os

dir_name_main = "my_project"
if not os.path.exists(dir_name_main):
    os.mkdir(dir_name_main)

my_project = ("settings", "mainapp", "authapp")
f_settings = ("__init__.py", "dev.py", "prod.py")
p_settings = os.path.join(dir_name_main, my_project[0])
f_app = ("__init__.py", "models.py", "views.py", "templates")
p_mainapp = os.path.join(dir_name_main, my_project[1])
p_authapp = os.path.join(dir_name_main, my_project[2])
[os.makedirs(os.path.join(dir_name_main, i)) for i in my_project if not os.path.exists(i)]
[os.makedirs(os.path.join(p_settings, name)) for name in f_settings if not os.path.exists(name)]
[os.makedirs(os.path.join(p_mainapp, name)) for name in f_app if not os.path.exists(name)]
[os.makedirs(os.path.join(p_authapp, name)) for name in f_app if not os.path.exists(name)]
templates = ("base.html", "index.html")
path_tem_m = os.path.join(p_mainapp, "templates")
path_tem_a = os.path.join(p_authapp, "templates")
[os.makedirs(os.path.join(path_tem_m, "mainapp"))]
new_path_m = os.path.join(path_tem_m, "mainapp")
[os.makedirs(os.path.join(new_path_m, i)) for i in templates if not os.path.exists(i)]
[os.makedirs(os.path.join(path_tem_a, "authapp"))]
new_path_a = os.path.join(path_tem_a, "authapp")
[os.makedirs(os.path.join(new_path_a, i)) for i in templates if not os.path.exists(i)]
