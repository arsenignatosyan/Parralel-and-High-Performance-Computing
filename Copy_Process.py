import os
import shutil
from concurrent.futures import ProcessPoolExecutor

def concat_copy_files(src, dest):
    src_file = os.listdir(src)
    
    executor = ProcessPoolExecutor(25)
    process = []
    
    for i in src_file:
        src_full = os.path.join(src, i)
        if os.path.isfile(src_full):
            temp = executor.submit(shutil.copy, src_full, dest)
            process.append(temp)
   
def main():
    src = "./"
    dest = "../files_threads"
    concat_copy_files(src, dest)
    

if __name__ == '__main__':
    	main()
