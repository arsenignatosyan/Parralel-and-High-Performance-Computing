import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def concat_copy_files(src, dest):
    src_file = os.listdir(src)
    
    executor = ThreadPoolExecutor(25)
    threads = []
    
    for i in src_file:
        src_full = os.path.join(src, i)
        if os.path.isfile(src_full):
            temp = executor.submit(shutil.copy, src_full, dest)
            threads.append(temp)

def main():
    src = "./"
    dest = "../files_threads"
    concat_copy_files(src, dest)
    

if __name__ == '__main__':
    	main()
