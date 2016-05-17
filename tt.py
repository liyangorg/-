
import matplotlib.pyplot as plt
import init
import algorithms
import figure
import common

#从文件获取点集合
points = init.read_points("points.json")
#单元格化处理
cell_info, cell_points_info = init.cell_deal(points, 10)

##标记点和中心节点
#plt.hold(True)
#for i, point in enumerate(points):
#		plt.scatter(point[0], point[1])
#figure.set_axes_grid()
#
#贪心算法解决
distance = algorithms.greedy_greedy(cell_info, cell_points_info)
print("greedy_greedy\t", end=':')
print(distance)


pass
