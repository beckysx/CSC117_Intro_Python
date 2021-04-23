# Xu Song
# Lab 28

import matplotlib.pyplot as plt

# Bar chart
myGraphValues = [20, 6, 2, 5, 9, 1]
myGraphWidths = [1, 0.7, 0.8, 1, 1, 1]
myGraphColors = ['r', '#FF6600', 'y', 'g', 'b', 'DarkViolet']
myGraphLabels = ['Dragon', 'Greyhound', 'Badger', 'Possum', 'Phoenix', 'Mongolian Wild Ass']

x = range(0, len(myGraphLabels))
plt.bar(x, myGraphValues, align='center', width=myGraphWidths, color=myGraphColors)
plt.title('Favorite Animals')
plt.ylabel('Number of People')
plt.xlabel('Animal')
plt.xticks(x, myGraphLabels)
plt.show()

# Pie chart
myGraphValues = [20, 6, 2, 5, 9, 1]
myGraphColors = ['r', '#FF6600', 'y', 'g', 'b', 'DarkViolet']
myGraphLabels = ['Dragon', 'Greyhound', 'Badger', 'Possum', 'Phoenix', 'Mongolian Wild Ass']
explode = (0, 0.2, 0, 0, 0, 0)
plt.pie(myGraphValues, colors=myGraphColors, labels=myGraphLabels, \
        explode=explode, autopct='%1.1f%%', counterclock=False, \
        shadow=True)
plt.title('Favorite Animals')
plt.show()

# Line Graphs
myGraphValues = [20, 6, 2, 5, 9, 1]
plt.plot(range(1, 7), myGraphValues)
plt.title('Temperatures')
ax = plt.axes()
ax.set_xlim([0, 10])
ax.set_ylim([-5, 50])
ax.set_xticks([1, 3, 5, 7])
ax.set_yticks([2, 4, 6, 8, 10])
ax.grid()
plt.show()

myGraphValues = [20, 6, 2, 5, 9, 1]
myOtherGraphValues = [5, 6, 9, 22, 3, 4]
plt.plot(range(len(myGraphValues)), myGraphValues, 'o-')
plt.plot(range(len(myOtherGraphValues)), myOtherGraphValues, 'D-')
plt.legend(['mice', 'dragons'], loc=2)
plt.title('Temperatures')
ax = plt.axes()
ax.grid()
plt.savefig('MySampleImage.png', format='png')
plt.show()
