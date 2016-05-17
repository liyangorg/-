import init
import algorithms
import figure
import common

import matplotlib.pyplot as plt
import numpy as np

points30 = init.create_points(30)
points200 = init.create_points(200)


#遗传算法
population_size = 300	#优化得到
start_point = [0, 0]
cross_rate = 0.9	#优化得到
gens = 300	#优化得到

#设置变量为种群数量
mutation_rate = list(np.arange(0.001, 0.2, 0.01))
distances1 = []
distances2 = []

for i, val in enumerate(mutation_rate):
		distance = algorithms.ga(points30, start_point, population_size, cross_rate, val, gens)
		distances1.append(distance)
		print(i,distance)
for i, val in enumerate(mutation_rate):
		distance = algorithms.ga(points200, start_point, population_size, cross_rate, val, gens)
		distances2.append(distance)
		print(i,distance)

plt.hold(True)
x = list(np.arange(0.001, 0.2, 0.01))
plt.plot(x,distances1, label=' 30 points')
plt.plot(x,distances2, label=' 200 points')
plt.legend(loc='upper left')

plt.title("find best mutation rate")
plt.xlabel("mutation rate")
plt.ylabel("length of route")
plt.show()


pass


