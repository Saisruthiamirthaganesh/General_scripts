# Python code to demonstrate creation of files and reading those files within the scope of Python as well as get their execution time.
#Importing pandas package to create dataframes and time package to get runtime
import pandas as pd
import time

#Printing start time of operation
start=time.asctime( time.localtime(time.time()) )
print(start)

#Specifying filename, writing columns into the dataframe in the file
filename = "data.txt"
with open((filename),'w') as f:
    df=pd.DataFrame(({"Name":['A','B','C','D','E'],"Age": ['18','25','31','11','52']}))
    dfas_string=df.to_string(header=False,index=False)
    f.write(dfas_string)
print(df)

#Printing the second column of the created dataframe
print(df.iloc[:,1])

#Printing stop time of operation
stop=time.asctime( time.localtime(time.time()) )
print(stop)
start=time.asctime( time.localtime(time.time()) )

#Printing start time of operation
print(start)

#Specifying filename, writing more columns into the dataframe in the file
filename2 = "data2.txt"
with open((filename2),'w') as f:
    df2=pd.DataFrame(({"Name":['A','B','C','D','E'],"Age": ['18','25','31','11','52'],"Gender":['Female','Female','Male','Female','Male'],"Location": ["Ukraine","Italy","India","United States","Ireland"],"Type of cancer":["Pancreatic","Breast","Melanoma","Ovarian","Glioma"],"Response time to medication(in seconds)":['15','11','21','9','10']}))
    df2as_string=df2.to_string(header=False,index=False)
    f.write(df2as_string)
print(df2)

#Printing the second column of the created dataframe
print(df2.iloc[:,1])

#Printing stop time of operation
stop=start=time.asctime( time.localtime(time.time()) )
print(stop)

