import os
import shutil

src = "./"
src_files = os.listdir(src)
dest = "../files_simple"


for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)
