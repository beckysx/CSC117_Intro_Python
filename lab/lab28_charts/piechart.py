#Xu Song
#pie chart
import matplotlib.pyplot as plt

file=open('piedata.txt','r')
line=file.readline()
line=line.rstrip('\n')
value=[]
while line!='':
    value.append(float(line))
    line=file.readline()
    line=line.rstrip('\n')
file.close()

mycolors=['peachpuff','g','salmon','slategray','palevioletred','skyblue','peru','khaki']
mylabels=['Java','C','C++','Python','Visual Basic','C#','JavaScript','Others']
plt.pie(value,colors=mycolors,labels=mylabels,autopct='%1.1f%%',counterclock=False,shadow=True)
plt.title('The most Popular Computer Languages')
plt.show()

    
