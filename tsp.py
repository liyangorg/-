import numpy as np
import matplotlib.pyplot as plt
import init
import algorithms
import figure
import common

#从文件获取点集合
points = init.read_points("points.json")
#单元格化处理
cell_info, cell_points_info = init.cell_deal(points, 10)

#遗传算法
start_point = [0, 0]
population_size = 300
cross_rate = 0.65
mutation_rate = 0.065
gens = 300

##单纯的使用GA算法，整体解决，不过结果有些异常
#distance = algorithms.ga(points, start_point, population_size, cross_rate, mutation_rate, gens)
#print("ga", end=':')
#print(distance)
#
##单纯的使用greedy算法，整体解决，结果正常
#route = algorithms.greedy(points, points[0])
#distance = common.cal_distance(route)
#print("greedy:", end=':')
#print(distance)
#
distances = []
#遗传算法解决
#distance = algorithms.ga_ga(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens)
#print("ga_ga\t", end=':')
#print(distance)
#distances.append(distance)
#

#贪心算法解决
distance = algorithms.greedy_greedy(cell_info, cell_points_info)
print("greedy_greedy\t", end=':')
print(distance)
distances.append(distance)

#cell内部greedy，cell外部GA
distance = algorithms.ga_greedy(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens)
print("ga_greedy\t", end=':')
print(distance)
distances.append(distance)

#cell内部GA，cell外部greedy
distance = algorithms.greedy_ga(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens)
print("greedy_ga\t", end=':')
print(distance)
distances.append(distance)


n_groups = 4
fix, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4

opacity = 0.4
rects = plt.bar(index, distances, bar_width,alpha=opacity, color='b',label='length of route')

plt.xlabel('algorithms')
plt.ylabel('distance')
plt.title('algorithms && distances')
plt.xticks(index + bar_width, ('ga2', 'greedy2', 'ga_greedy', 'greedy_ga'))
plt.legend()

plt.tight_layout()
plt.show()

pass
