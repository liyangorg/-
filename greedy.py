import matplotlib.pyplot as plt

import init
import common
import algorithms

#设置不同的数目的点集合
NUMS = list(range(10,500,10))

start_point = [0, 0]
population_size = 300
cross_rate = 0.65
mutation_rate = 0.065
gens = 300

distances1 = []
distances2 = []
distances3 = []
distances4 = []
ideal_distances = []
for i, val in enumerate(NUMS):
		points = init.create_points(val)
		cell_info, cell_points_info = init.cell_deal(points, 10)

		print(val)
		#贪心算法
		distance = algorithms.greedy_greedy(cell_info, cell_points_info)
		distances1.append(distance)

		#遗传算法
		distance = algorithms.ga_ga(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens)
		distances2.append(distance)


		#cell内部greedy，cell外部GA
		distance = algorithms.ga_greedy(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens)
		distances3.append(distance)

		#cell内部GA，cell外部greedy
		distance = algorithms.greedy_ga(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens)
		distances4.append(distance)
plt.figure()
plt.hold(True)
plt.plot(NUMS, distances1,color='r',linewidth=2.5, linestyle='-',label='greedy2')
plt.plot(NUMS, distances2,color='b',linewidth=2.5, linestyle='-',label='ga2')
plt.plot(NUMS, distances3,color='y',linewidth=2.5, linestyle='-',label='ga_greedy')
plt.plot(NUMS, distances4,color='k',linewidth=2.5, linestyle='-',label='greedy_ga')
plt.legend(loc='upper left')

plt.xlabel('number of point(points)')
plt.ylabel('length of route(meters)')
plt.title('Comparing four kinds of algorithms')

#ax = plt.axes()
#ax.set_xlim(0, 500)
#ax.xaxis.set_major_locator(plt.MultipleLocator(50))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
#
plt.show()
