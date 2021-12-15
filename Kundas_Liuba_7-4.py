import os
from collections import defaultdict, Counter
import django

root_dir = django.__path__[0]
dir_f = defaultdict(int)
#small_f = [item.stat().st_size % 2 ** 10 for item in os.scandir("some_data")]
#counter = Counter("some_data")
for root, dirs, files in os.walk(root_dir):
    for file in files:
        f_size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        dir_f[f_size] += 1

for f_size, numbers in sorted(dir_f.items()):
    print(f'{f_size}: {numbers}')
