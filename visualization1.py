import matplotlib.pyplot as plt

#scatter graph
fig = plt.figure("Scatter")
ax = fig.add_subplot(1,1,1)
ax.scatter([-1, 0, 2, 3, 5], [2, 1, 3, 0.5, 4])
plt.show()


#bubble graph, its scatter with more parameters
fig1 = plt.figure("Scatter")
ax1 = fig1.add_subplot(1,1,1)
#parameters: x, y, bubble_widths, bubble color
ax1.scatter([-1, 0, 2, 3, 5], [2, 1, 3, 0.5, 4], [120, 200, 300, 150, 30], ['r', 'g', 'b', 'y'])
plt.show()

#pie char

fig2 = plt.figure("Pie")
sizes = [50, 50, 44, 36]
labels = ["Wade", "James", "Kobe", "Curry"]
explode = (0.1,0,0,0)
colors = ["red", "purple", "yellow", "blue"]
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.show()