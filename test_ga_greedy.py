import matplotlib.pyplot as plt

import init
import common
import algorithms

#设置不同的数目的点集合
NUMS = list(range(10,500,10))

distances = []
ideal_distances = []
for i, val in enumerate(NUMS):
		points = init.create_points(val)

		#理想贪心
		route = algorithms.greedy(points, points[0])
		ideal_distance = common.cal_distance(route)
		ideal_distances.append(ideal_distance)

		#遗传算法

plt.hold(True)
plt.plot(distances)
plt.plot(ideal_distances)


#ax = plt.axes()
#ax.set_xlim(0, 500)
#ax.xaxis.set_major_locator(plt.MultipleLocator(50))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
#
plt.show()
