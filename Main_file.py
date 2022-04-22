import os
from tqdm.gui import tqdm_gui
#from ComputeResult_files_C1 import compute_c1
global filepath
try:
    def loadcase(fpath):
        print("entering the main file module")
        loadcase1=['C1','C4','C5','C6','C7','C8','C9','B11','B22']
        #loadcase=['C1','C4','C5']
        #----- getting the path of source python file
        ssource = __file__
        ss=os.path.dirname(ssource)
        path = ss + '\ComputeResult_files_'
        print(path)
        filepath=fpath
        print(filepath)
        #filepath1 = compute_c1(fpath)

        for i in tqdm_gui(loadcase1):
            #print(i)
           # filepath =compute_c1(filepath)
            #C:\Users\stephen.arput\PycharmProjects\fatigue
            #path='C:/Users/stephen.arput/Documents/RESULTS/LOC222/ComputeResult_files_'


            #path = 'C:/Users/stephen.arput/PycharmProjects/fatigue/ComputeResult_files_'
            ls='python '+path+i+'.py'

            os.system(ls)

        return ('Completed the Result computation for various load cases')

except Exception as e:
    print('The Exception message is: ', e)


