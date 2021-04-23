#Xu Song
#linechart

import matplotlib.pyplot as plt


#read firstline,convert to list
linedata=open('linedata.txt','r')
line=linedata.readline()
line=line.rstrip('\n')
line=line.split(',')
rop=[]
for number in line:
    rop.append(int(number))
    
#read second line,conver to list    
line=linedata.readline()
line=line.rstrip('\n')
line=line.split(',')
dem=[]
for number in line:
    dem.append(int(number))

linedata.close()

#make line graph
ropValue=rop
demValue=dem
plt.plot(range(1,len(ropValue)+1),ropValue,'o-')
plt.plot(range(1,len(demValue)+1),demValue,'o-')
plt.legend(['Rop','Dem'],loc=2)
plt.title('2018 California Election Results in First Four Districts')
plt.xlabel('Districts')
plt.ylabel('Number of votes')
ax=plt.axes()
ax.grid()
ax.set_xticks([1,2,3,4])
plt.show()



