import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import math
from scipy import *

columns = ['dayOfYr', 'time','tideHeight']

df = pd.read_fwf(r'ASTR19_S22_group_project_data.txt', header = None, skiprows=(0,1,2), names = columns)
df.head()

ti = df['time']
dy = df['dayOfYr']
h = df['tideHeight']

# plotting first graph
plt.plot(dy, h)

# sinodial function
def sinVal(x):
    arr=[]
    for z in x:
        arr.append(math.sin(z))
    return arr


# Best fit 

osci = np.linspace(1,12*math.pi,100)

sinValArr = sinVal(osci)

plt.scatter(osci, sinValArr)
plt.plot(dy, h)

# Adhiraj Singh dummy residual analysis code does not work - 
# plotting residuals
df['remainderVal'] = df['tideHeight'] - df['myfitmodelVals']
plt.plot(df['smoothTime'], df['remainderVal'])
plt.title('Residual values graphed against time')

# histogram
plt.hist(df['remainderVal'], bins = 16, label = 'residuals in data', alpha = 0.5, rwidth = 0.6)
plt.xlabel('Error')
plt.ylabel('Frequenct')










