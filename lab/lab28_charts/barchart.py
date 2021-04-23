# Xu Song
# Barchart

import matplotlib.pyplot as plt

file = open('piedata.txt', 'r')
line = file.readline()
line = line.rstrip('\n')
value = []
while line != '':
    value.append(float(line))
    line = file.readline()
    line = line.rstrip('\n')
file.close()

mycolors = ['maroon', 'firebrick', 'indianred', 'salmon', 'tomato', 'orangered', 'coral']
mylabels = ['Chinese', 'Spanish', 'English', 'Arabic', 'Hindi', 'Bengali', 'Portugues']
x = range(0, len(value))
plt.bar(x, value, align='center', width=0.8, color=mycolors)
plt.title('The most spoken Languages Worldwide(native speakers in millions)')
plt.ylabel('Speaker in million')
plt.xlabel('Language')
plt.xticks(x, mylabels)
ax = plt.axes()
ax.set_ylim([0, 200])
plt.show()
