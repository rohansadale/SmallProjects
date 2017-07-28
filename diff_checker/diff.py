'''
To run:
    python diff.py folder1 folder2 log_folder_name

usage: diff.py [-h] [-f1 FOLDER1] [-f2 FOLDER2] [-l LOG]

Difference between same name files in two folders

optional arguments:
      -h, --help            show this help message and exit
      -f1 FOLDER1, --folder1 FOLDER1
                                Folder 1 location
      -f2 FOLDER2, --folder2 FOLDER2
                                Folder 2 location
      -l LOG, --log LOG     Log folder location

+ All files from folder1 are read. Only files with '.' in their name are considered
+ The above files from folder1 are compared to same name files in folder2
+ Log output in log_folder_name 

'''

import sys
import os
import argparse

def get_diff(file1, file2, f):
    os.system('diff ' + file1 + ' ' + file2 + ' > ' + log_f)

def get_files(folder_name):
    files = []
    for f in os.listdir(folder_name):
      if '.' in f:
          files.append(f)
    return files

def args_parser():
    parser = argparse.ArgumentParser(description = "Difference between same name files in two folders")
    parser.add_argument("-f1", "--folder1", help="Folder 1 location")
    parser.add_argument("-f2", "--folder2", help="Folder 2 location")
    parser.add_argument("-l", "--log", help="Log folder location")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = args_parser()
    folder_1 = args.folder1
    folder_2 = args.folder2
    log_folder = args.log
    files = get_files(folder_1)
    for f in files:
        f1 = folder_1 + '/' + f
        f2 = folder_2 + '/' + f
        log_f = log_folder + '/' + f + '.log'
        get_diff(f1, f2, log_f)
