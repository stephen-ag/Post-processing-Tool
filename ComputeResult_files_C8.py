import os
import glob
import pandas as pd

os.chdir("C:/Users/stephen.arput/Documents/RESULTS/LOC222/LOC2")

filenames= os.listdir (".") # get all files' and folders' names in the current directory

folder = []
for filename in filenames: # loop through all the files and folders
    if os.path.isdir(os.path.join(os.path.abspath("."), filename)): # check whether the current object is a folder or not
        folder.append(filename)

for j in folder:
    if j=='C8':
        
        os.chdir("C:/Users/stephen.arput/Documents/RESULTS/LOC222/LOC2/"+ j)
        ###---------------------------------------------------------------------------------------------------------

        li=os.listdir (".") 
        for i in li:
            print(i,"completed")
            os.chdir(i)
            
            #os.chdir("path11")
            name =os.path.basename(os.getcwd())
            ss =pd.read_excel('concated_'+i+'.xlsx')
            ##ss =pd.read_excel('concated_path11.xlsx')
            ## LC1=[A], lC2=[B]...etc
            loadcase = []
            i=1
            #loadcase =['[A]','[B]','[C]']--- FOR VALVE BODY
            loadcase = ['[B]', '[C]', '[D]']
            #loadcase =['[A]','[B]','[C]','[D]','[E]']
            #loadcase =['[A]','[B]','[C]','[D]','[E]','[F]','[G]','[H]','[I]','[J]','[K]','[L]','[M]']...for C1

            for lc in loadcase:
                LC=ss.loc[:, ss.columns.str.startswith(lc)]
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
            c8d = filenames[1]-filenames[0]
            c8d.columns= column_list
            c8d.to_excel('c8d_'+name+'.xlsx',sheet_name='input',index = False)

            c8_c21u = filenames[2]-filenames[1]
            c8_c21u.columns=column_list
            c8_c21u.to_excel('c8_c21u_'+name+'.xlsx',sheet_name='input',index = False)

            os.chdir("../")
