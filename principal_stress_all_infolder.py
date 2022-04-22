import os
import glob
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from pathlib import Path
import pandas as pd
from tqdm.gui import tqdm_gui
global fpath

try:


    def principal(fpath):
        print('Entering principal stress module')
        try:

            #os.chdir("C:/Users/stephen.arput/Documents/RESULTS/LOC222/LOC2")
            os.chdir(fpath)
            results_folder =['Results_path11','Results_path22','Results_path33']
            for rfile in tqdm_gui(results_folder):
                os.chdir(rfile)

                filenames= os.listdir (".") # get all files' and folders' names in the current directory
                ddff=[]

                for file in filenames:
                    components = pd.read_excel(file,sheet_name='input')
                    components = components[components.filter(regex='^(?!Unnamed)').columns]
                    sumI=components.σxx+components.σyy+components.σzz
                    prodI=components.σxx*components.σyy*components.σzz

                    #----------- calculating the total number of rows from the input sheet
                    n=components.shape[0]

                    ##-----------calculating the stress invariant I1,I2 and I3
                    I1= sumI
                    I2=(components.σxx*components.σyy)+(components.σyy*components.σzz)+(components.σxx*components.σzz)-components.τxy**2-components.τyz**2-components.τzx**2
                    df = components
                    I3 =(df.σxx*df.σyy*df.σzz)-(df.σxx*df.τyz**2)-(df.σyy*df.τzx**2)-(df.σzz*df.τxy**2)+(2*df.τxy*df.τyz*df.τzx)

                    df1=pd.DataFrame()

                    df1["I1"]=I1
                    df1["I2"]=I2
                    df1["I3"]=I3


                    ##----------- Calculating the Principal stress from the invariants I1,I2 and I3 of eqation of the type: AX³+Bx²+CX+D = 0 where A=1, B is -ve and D is -ve'
                    L=[]
                    for i in range(n):
                        aa=df1.loc[i].to_list()
                        rt=np.roots([1,-aa[0],aa[1],-aa[2]])
                        L.append(rt)

                    ##----------- converting the Principal stress from the loop, from array to dataframe.
                    my_array = np.array(L)
                    df3 = pd.DataFrame(my_array, columns = ['Sigma_1','Sigma_2','Sigma_3'])
                    df3['difference1']= pd.Series.abs(df3['Sigma_1']-df3['Sigma_2'])
                    df3['difference2']= pd.Series.abs(df3['Sigma_2']-df3['Sigma_3'])
                    df3['difference3']= pd.Series.abs(df3['Sigma_3']-df3['Sigma_1'])

                    df4=df3[['difference1','difference2','difference3']]
                    df3['Max_difference']=df4.max(axis=1)
                    ##----------- joining the results from each of the dataframes
                    results1=components.join(df1)
                    results2=results1.join(df3)
                    dfmax= results2
                    ff=dfmax.loc[dfmax['Max_difference'].idxmax()]
                    #ddff=ddff.join(ff)
                    #ddff.merge(ff, how = 'left')
                    #ddff.append(ff)
                    #lll=pd.concat([ff])
                    ddff.append(ff)

                    ##----------- exporting the final results to excelfile
                    results2.to_excel('principal_stress_'+file)

                    print("completed principal stress for file " + file)
                basename=[]
                for file in filenames:
                    a,b=file.split(".")
                    basename.append(a)
                summy= pd.DataFrame(ddff,index=basename)

                summy.to_excel(rfile +'summary.xlsx')
                os.chdir("../")
            return ('Completed the Principal Stress computation for all load cases')

        except Exception as e:
            return('The Exception message is: :\n ', e)

except Exception as e:
    print('The Exception message is:\n', e)
