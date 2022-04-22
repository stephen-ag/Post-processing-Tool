#### Macro to compute the delta difference between the load sets...for path11. change to path22 and path33 accordingly###---
import os
import glob
import pandas as pd

global fpath
def compute_c1():

    os.chdir("C:/Users/stephen.arput/Documents/RESULTS/LOC222/LOC2")

    #os.chdir(fpath)

    filenames= os.listdir (".") # get all files' and folders' names in the current directory

    folder = []
    for filename in filenames: # loop through all the files and folders
        if os.path.isdir(os.path.join(os.path.abspath("."), filename)): # check whether the current object is a folder or not
            folder.append(filename)

    for j in folder:
        if j=='C1':

            os.chdir("C:/Users/stephen.arput/Documents/RESULTS/LOC222/LOC2/"+ j)

            li=os.listdir (".")
            for i in li:
                print(i)
                os.chdir(i)

            ###---------------------------------------------------------------------------------------------------------

                #os.chdir("path11")
                name =os.path.basename(os.getcwd())
                ss =pd.read_excel('concated_'+i+'.xlsx')
                #ss =pd.read_excel('concated_path11.xlsx')

                i=1
                #loadcase =['[A]','[B]','[C]']
                loadcase =['[B]','[C]','[D]','[E]','[F]','[G]','[H]','[I]','[J]','[K]','[L]','[M]','[N]']

                for lc in loadcase:
                    LC=ss.loc[:, ss.columns.str.startswith(lc)]
                    # the location corresponds to x,y,z,xy,yz,zx =(0,3,5,1,4,2) for A, B,etc
                    LC=LC.iloc[:,[0,3,5,1,4,2]]
                    LC.to_csv('LC_'+str(i)+'.csv', header=False, index=False)
                    i=i+1

                filenames=[]
                # Collecting all the file name staring wit LC_ and form a list of it.##--------
                for file in glob.glob("LC_*.csv"):
                    filenames.append(file)
                j=0
                n=len(loadcase)
                #__________looping thorugh all the load case files and storing in dataframe for next calculation.
                for i in range(1,n+1):
                    filenames[j]=pd.read_csv('LC_'+str(i)+'.csv',header=None)
                    j=j+1

                # calculating the difference delta values for each stress component for all points along the paths
                # check for the group of families and input the equation as required.
                column_list = ['σxx','σyy','σzz','τxy','τyz','τzx']
                c1u = filenames[1]-filenames[0]
                c1u.columns= column_list
                c1u.to_excel('c1u_'+name+'.xlsx',sheet_name='input',index = False)

                c21u = filenames[2]-filenames[1]
                c21u.columns=column_list
                c21u.to_excel('c21u_'+name+'.xlsx',sheet_name='input',index = False)

                c22u = filenames[4]-filenames[3]
                c22u.columns=column_list
                c22u.to_excel('c22u'+name+'.xlsx',sheet_name='input',index = False)

                c31u = filenames[5]-filenames[4]
                c31u.columns=column_list
                c31u.to_excel('c31u_'+name+'.xlsx',sheet_name='input',index = False)

                c32u = filenames[6]-filenames[5]
                c32u.columns=column_list
                c32u.to_excel('c32u_'+name+'.xlsx',sheet_name='input',index = False)

                c32d = filenames[7]-filenames[6]
                c32d.columns=column_list
                c32d.to_excel('c32d_'+name+'.xlsx',sheet_name='input',index = False)

                c31d = filenames[8]-filenames[7]
                c31d.columns=column_list
                c31d.to_excel('c31d_'+name+'.xlsx',sheet_name='input',index = False)

                c22d = filenames[9]-filenames[8]
                c22d.columns=column_list
                c22d.to_excel('c22d'+name+'.xlsx',sheet_name='input',index = False)

                c21d = filenames[11]-filenames[10]
                c21d.columns=column_list
                c21d.to_excel('c21d_'+name+'.xlsx',sheet_name='input',index = False)

                c1d = filenames[12]-filenames[11]
                c1d.columns= column_list
                c1d.to_excel('c1d_'+name+'.xlsx',sheet_name='input',index = False)

                os.chdir("../")
                print("compute C1 completed")
compute_c1()