# -------------------macro to read all the folder and create a concatenate.xls file for all  the cases c1 to C9 @ each LOC1. change the path accordingly

import os
import glob
from tqdm.gui import tqdm_gui
from tqdm.gui import tqdm_gui
from tqdm import tqdm
from matplotlib import pyplot as plt
import pandas as pd
#from postprocessing import submit
global fpath
def concat(fpath):
    try:
        print("entered concat module")
        os.chdir(fpath)

        filenames= os.listdir (".") # get all files' and folders' names in the current directory

        folder = []
        for filename in filenames: # loop through all the files and folders
            if os.path.isdir(os.path.join(os.path.abspath("."), filename)): # check whether the current object is a folder or not
                folder.append(filename)
        print('Entering folder looping')
        for j in tqdm_gui(folder):
            os.chdir(fpath +'/'+j)
            ###---------------------------------------------------------------------------------------------------------

            os.chdir("path11")
            file_extension = ".xls"
            all_files = [i for i in glob.glob(f'*{file_extension}')]

            ###------------------macro to read all the files in a folder and concatenate to single file and saved to excel for each path11,path22, path33---------------
            ##dff = pd.read_csv('Normall-stress_X.txt' ,delimiter = "\t",index_col=None,  encoding = "ISO-8859-1")

            aaa=[pd.read_csv(file ,delimiter = "\t",index_col=None, encoding = "ISO-8859-1").drop(["Unnamed: 0"],axis=1) for file in all_files]

            ccc=pd.concat(aaa,axis=1)

            ccc.to_excel('concated_path11.xlsx')
            print("completed export of excel for path11")
            ###---------------------------------------------------------------------------------------------------------

            os.chdir("../path22")
            file_extension = ".xls"
            all_files = [i for i in glob.glob(f'*{file_extension}')]

            ###------------------macro to read all the files in a folder and concatenate to single file and saved to excel for each path11,path22, path33---------------
            ##dff = pd.read_csv('Normall-stress_X.txt' ,delimiter = "\t",index_col=None,  encoding = "ISO-8859-1")

            aaa=[pd.read_csv(file ,delimiter = "\t",index_col=None, encoding = "ISO-8859-1").drop(["Unnamed: 0"],axis=1) for file in all_files]

            ccc=pd.concat(aaa,axis=1)

            ccc.to_excel('concated_path22.xlsx')
            print("completed export of excel for path22")
        ###---------------------------------------------------------------------------------------------------------

            os.chdir("../path33")
            file_extension = ".xls"
            all_files = [i for i in glob.glob(f'*{file_extension}')]

        ###------------------macro to read all the files in a folder and concatenate to single file and saved to excel for each path11,path22, path33---------------
        ##dff = pd.read_csv('Normall-stress_X.txt' ,delimiter = "\t",index_col=None,  encoding = "ISO-8859-1")

            aaa=[pd.read_csv(file ,delimiter = "\t",index_col=None, encoding = "ISO-8859-1").drop(["Unnamed: 0"],axis=1) for file in all_files]

            ccc=pd.concat(aaa,axis=1)

            ccc.to_excel('concated_path33.xlsx')
            print("completed export of excel for path33")
        ###---------------------------------------------------------------------------------------------------------


        greetings =f'Concatenation of files completed in path \n:  {fpath}'
        return greetings

    except Exception as e:
        return('The Exception message is: \n', e)