import re

print(dir(re))
re_dir_list = []
for entry in dir(re):
    if "find" in entry:
        re_dir_list.append(entry)

print(sorted(re_dir_list))