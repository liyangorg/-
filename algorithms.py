#自定义模块
import common
import figure
import ga_init

import random
import matplotlib.pyplot as plt


"""
func:贪心算法
"""
def greedy(points, start_point):

		all_points = [start_point] + points	#含有起始点的点集合
		dis_matrix = common.cal_distance_matrix(all_points)
		dis_matrix_seq = common.cal_sequenced_distance_matrix(all_points)
		walked = [0]*len(dis_matrix_seq)	#用来做访问过的无线设备节点的标

		#为点创建序号，以便于后续工作
		dic_points = {}
		for i, point in enumerate(all_points):
				dic_points[i] = all_points[i]

		route_index = [0]	#route的第一个节点，或者这样子route = [all_points[0]]
		walked[0] = 1

		#贪心算法解决tsp问题核心算法
		temp = 0
		while 0 in walked:
				for i, val in enumerate(dis_matrix_seq[temp]):
								if i > 0:
									if walked[val] == 0:
										route_index.append(val)
										temp = val
										walked[temp] = 1
										break
									else:
										pass
								else:
									pass
		#根据节点标号映射节点坐标						1
		route = [[0,0]] * len(route_index)
		for i, val in enumerate(route_index):
			route[i] = dic_points[val]

		return  route


"""
func:遗传算法
"""
def ga(points, start_point, population_size, cross_rate, mutation_rate, gens):
		population, distances, route = ga_init.ga(points, start_point, population_size, cross_rate, mutation_rate, gens)
		distance = distances[-1]['min']
		return distance

"""
func:内部外部均为贪心算法
"""
def greedy_greedy(cell_info, cell_points_info):
	#作图准备工作

	fig = plt.figure()
	plt.hold(True)
	ax = fig.add_subplot(111)

   #显示点集合
	for i, val in enumerate(cell_points_info):
			for j, point in enumerate(cell_points_info[val]):
					plt.scatter(point[0], point[1])
	#标记单元格
	figure.fill_cell(cell_info,ax)
	for i, val in enumerate(cell_info):
			plt.scatter(cell_info[val][0], cell_info[val][1], marker='x', color='r')
	#plt.title('algorithms about route')
	#plt.title("cell of area")


	#进行cell之间的greedy算法
	cells = [[0,0]]*len(cell_info)
	for i, val in enumerate(cell_info):
		cells[val] = cell_info[val]
	cell_route = greedy(cells, cells[0])


	#cell内部确定路线，并且按照cells_route的顺序进行cell间的遍历
	route = []
	for i, v1 in enumerate(cell_route):
			for j, v2 in enumerate(cell_info):
					if v1 == cell_info[v2]:
							start_point = v1
							points = cell_points_info[v2]
							temp = greedy(points, start_point)
							for i, val in enumerate(temp):
									route.append(val)
					else:
							pass

	#标记cell的遍历顺序
	for i, val in enumerate(cell_route):
		if i == 0:
				pass
		else:
			plt.text(cell_route[i][0]+2, cell_route[i][1]+2, i)
   #基点的路径规划
	figure.paint_route(cell_route)

	#完整的路径规划
	figure.paint_route(route)
	figure.set_axes_grid()
	plt.xlabel('x(meters)')
	plt.ylabel('y(meters)')
	#plt.title("route of basic point")
	plt.show()

	#计算飞行距离
	distance = common.cal_distance(route)

	return distance

"""
func:cell内外均使用GA算法
"""
def ga_ga(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens):
		#进行cell之间的GA算法
		cells = [[0,0]] * len(cell_info)
		for i, val in enumerate(cell_info):
				cells[val] = cell_info[val]
		#GA算法求出cell之间的最短距离
		cell_route_distance = ga(cells, cells[0], population_size, cross_rate, mutation_rate, gens)

		#所有cell内部的路径长度
		distance_cell_inner = 0
		for i, val in enumerate(cell_points_info):
				distance_cell_inner += ga(cell_points_info[val], cell_info[val], population_size, cross_rate, mutation_rate, gens)

		#最短总路径
		distance = cell_route_distance + distance_cell_inner

		return distance

""""
func：cell内部使用greedy，cell外部使用GA
"""
def ga_greedy(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens):
		#进行cell外部的GA算法
		cells = [[0,0]] * len(cell_info)
		for i, val in enumerate(cell_info):
				cells[val] = cell_info[val]
		cell_route_distance = ga(cells, cells[0], population_size, cross_rate, mutation_rate, gens)

		#进行cell内部的greedy算法
		distance_cell_inner = 0
		for i, val in enumerate(cell_points_info):
				route = greedy(cell_points_info[val], cell_info[val])
				distance_cell_inner += common.cal_distance(route)

		#最短总路径
		distance = cell_route_distance + distance_cell_inner

		return distance

""""
func：cell内部使用GA，cell外部使用greedy
"""
def greedy_ga(cell_info, cell_points_info, population_size, cross_rate, mutation_rate, gens):
		#进行cell外部的greedy算法
		cells = [[0,0]]*len(cell_info)
		for i, val in enumerate(cell_info):
				cells[val] = cell_info[val]
		cell_route = greedy(cells, cells[0])
		cell_route_distance = common.cal_distance(cell_route)

		#进行cell内部的GA算法
		distance_cell_inner = 0
		for i, val in enumerate(cell_points_info):
				distance_cell_inner += ga(cell_points_info[val], cell_info[val], population_size, cross_rate, mutation_rate, gens)

		#最短总路径
		distance = cell_route_distance + distance_cell_inner

		return distance

