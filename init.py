import json
import random

"""
功能：于指定区域随机产生nums个一定范围内的点，并且返回坐标
"""
def create_points(nums):
		random.seed()
		area_start = 11
		area_end   = 80
		area_step  = 3
		points = [[random.randrange(area_start, area_end, area_step),random.randrange(area_start, area_end, area_step)] for val in range(nums)]
		return points

"""
func:把点集合写到文件
"""
def write_points(points, filename):
		data = {
						"Nums" : len(points),
						"Points" : points
						}
		with open("points.json", "w") as f:
				json.dump(data,f)


""""
func:从文件里读取点集合
"""
def read_points(filename):
		with open(filename) as handle:
				data = json.load(handle)
		points = data["Points"]

		return points

"""
func:判断给定的点在哪个cell中并返回key，若不在任何一个cell中，则返回-1
"""
def judge_point_cell(point, cell_info, cell_standard):
		for i, key in enumerate(cell_info):
				x= int(point[0] / cell_standard)*10 + 5    #根据点的坐标计算所在单元格的中心节点坐标
				y= int(point[1] / cell_standard)*10 + 5
				cell = [x, y]
				if cell_info[key] == cell:
						return key
				else:
						pass
		return -1

"""
func:对给定的点集合进行单元化处理，并返回处理后的cell与point的信息
"""
def cell_deal(points, cell_standard):
		cell_info = {}
		cell_points_info = {}
		cells = []

		#计算cell的中心节点有哪些
		for i, val in enumerate(points):
				x= int(points[i][0] / cell_standard)*10 + 5    #根据点的坐标计算所在单元格的中心节点坐标
				y= int(points[i][1] / cell_standard)*10 + 5
				if [x, y] in cells:    #判断此中心节点是否已经统计过
						pass
				else:
						cells.append([x, y])
		#计算cell_info
		for i, val in enumerate(cells):
				cell_info[i] = val

		#计算cell_points_info
		for i, key in enumerate(cell_info):
				temp = []    #临时存储一个cell中的points
				for j, point in enumerate(points):
						if judge_point_cell(point, cell_info, cell_standard) == key:
								temp.append(point)
						else:
								pass
				cell_points_info[key] = temp

		return cell_info, cell_points_info


