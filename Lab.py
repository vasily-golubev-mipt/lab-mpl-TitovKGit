import matplotlib.pyplot as plt
from numpy import *
import time
import imageio 
import os
import pandas as pd
#1

try:
    with open(input(),'r', encoding = "utf-8") as f:
        data = f.read().split('\n')
except:
    pass
for i in range(1, len(data)):
    data[i] = (data[i]).split(' ')
x = []
y = []
for i in range(1, int(data[0]) + 1):
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))
N = (max(x) - min(x))/(max(y) - min(y))
plt.subplot(N,1,1)
plt.scatter(x, y)
plt.axis([min(x) - 10, max(x) + 10, min(y) - 10, max(y) + 10])
plt.title(f'Number of points: {data[0]}')
plt.show()
print(x, y)

#2

d = input()
try:
    with open(d,'r', encoding = "utf-8") as f:   
        data = (f.read().split('\n'))
except:
    pass

try:
    with open(d,'r', encoding = "utf-8") as f: 
        count = (f.read().split())
except:
    pass    
   
count_ = []
for i in count:
    count_.append(double(i))
x = []
y = []
for i in range (len(data)):
    if (i + 1) % 2 == 0:
        y += ([double(data[i].split())])
    else: 
        x += ([double(data[i].split())])
frame = []
for i in range(len(x) - 1):
    plt.axis([0, max(count_), min(count_) - abs(min(count_)/5), max(count_) + abs(max(count_)/5)])
    plt.plot(x[i],y[i], color = 'g')
    plt.grid(True)
    plt.title(f'Frame: {i + 1}') 
    plt.savefig(f'{i+1}.png')
    frame.append(f'{i+1}.png')
    plt.clf()
    
with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in frame:
        image = imageio.imread(filename)
        writer.append_data(image)
    for filename in frame:
        os.remove(filename)

os.startfile(r'mygif.gif')
time.sleep(2)
os.remove('mygif.gif')

#3
dk = pd.read_csv('students.csv', sep=";", header= None)
dk.columns = ['prep','group', 'marks']
test5 = dk.groupby(['prep', 'marks'])['prep'].count().unstack('marks').fillna(0)
test6 = dk.groupby(['group', 'marks'])['group'].count().unstack('marks').fillna(0)
ax = test5.plot(kind='bar', stacked=True, rot= 0)
bx = test6.plot(kind='bar', stacked=True, rot= 0)
plt.show()

   
