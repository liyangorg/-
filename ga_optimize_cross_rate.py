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
cross_rate = 0.9
mutation_rate = 0.01
gens = 300	#优化得到

#设置变量为种群数量
cross_rate = list(np.arange(0, 1, 0.05))
distances1 = []
distances2 = []


for i, val in enumerate(cross_rate):
		distance = algorithms.ga(points30, start_point, population_size, val, mutation_rate, gens)
		distances1.append(distance)

for i, val in enumerate(cross_rate):
		distance = algorithms.ga(points200, start_point, population_size, val, mutation_rate, gens)
		distances2.append(distance)

plt.hold(True)
plt.plot(x,distances1, label=' 30 points')
plt.plot(x,distances2, label=' 200 points')
plt.legend(loc='upper left')
x = list(np.arange(0, 1, 0.05))

plt.title("find best cross rate")
plt.xlabel("cross rate")
plt.ylabel("length of route")
plt.show()


pass


