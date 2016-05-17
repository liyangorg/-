import init
import algorithms
import figure
import common

import matplotlib.pyplot as plt

points30 = init.create_points(30)
points200 = init.create_points(200)

#遗传算法
start_point = [0, 0]
population_size = 300
cross_rate = 0.9
mutation_rate = 0.01
gens = 100

#设置变量为种群数量
gens = list(range(100,500,50))
distances1 = []
distances2 = []

for i, val in enumerate(gens):
		distance = algorithms.ga(points30, start_point, population_size, cross_rate, mutation_rate, val)
		distances1.append(distance)
for i, val in enumerate(gens):
		distance = algorithms.ga(points200, start_point, population_size, cross_rate, mutation_rate, val)
		distances2.append(distance)

plt.hold(True)
x = list(range(100,500,50))
plt.plot(x,distances1, label=' 30 points')
plt.plot(x,distances2, label=' 200 points')

plt.title("find best evolution gens")
plt.xlabel("evolution gens")
plt.ylabel("length of route")
plt.legend(loc='upper left')
plt.show()


pass


