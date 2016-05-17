import init
import algorithms
import figure
import common

import matplotlib.pyplot as plt


points30 = init.create_points(30)
points200 = init.create_points(200)

#遗传算法
start_point = [0, 0]
cross_rate = 0.9
mutation_rate = 0.01
gens = 100

#设置变量为种群数量
population_size = list(range(10,500,10))
distances1 = []
distances2 = []

for i, val in enumerate(population_size):
		distance = algorithms.ga(points30, start_point, val, cross_rate, mutation_rate, gens)
		distances1.append(distance)
for i, val in enumerate(population_size):
		distance = algorithms.ga(points200, start_point, val, cross_rate, mutation_rate, gens)
		distances2.append(distance)
plt.hold(True)
x = list(range(10,500,10))
plt.plot(x,distances1, label=' 30 points')
plt.plot(x,distances2, label=' 200 points')
plt.legend(loc='upper left')

plt.title("find best population size")
plt.xlabel("population size")
plt.ylabel("length of route")
plt.show()


pass


