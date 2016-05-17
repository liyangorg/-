
"""
func：计算给定点集合的距离矩阵
"""
def cal_distance_matrix(points):
    dis_matrix = [[0.0]*len(points) for i in range(len(points))]
    for n, point1 in enumerate(points):
        for m, point2 in enumerate(points):
            dis = lambda x1, y1, x2, y2 : ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            dis_matrix[n][m] = dis(point1[0], point1[1], point2[0], point2[1])
    return dis_matrix

"""
func:获取行有序距离矩阵
"""
def cal_sequenced_distance_matrix(points):
		dis_matrix = cal_distance_matrix(points)
		dis_sequence = []
		#获取行有序的距离矩阵 
		for i, val in enumerate(dis_matrix):
			temp = val.copy()	#val实为引用，不可以直接对其直接操作，否则会修改dis_matrix的值
			temp.sort()		#直接在list类型的line上操作
			dis_sequence.append(temp)

		#获取行有序的单元号矩阵
		#遍历行有序矩阵的每一行
		sequenced_distance_matrix = []
		for i, val in enumerate(dis_sequence):
			Point = []	#一个单元格到其他单元格的远近顺序
			line = []	#临时变量以防修改dis_sequence---行有序距离矩阵的一行
			line = val.copy()
			temp = []	#临时变量以防修改dis_matrix----初始距离矩阵的一行
			temp = dis_matrix[i].copy()
			#遍历行有序矩阵的每一行中的距离
			for j, dis in enumerate(line):
				seq = temp.index(dis)	#dis这个距离，在原始矩阵dis_matrix对应行的位置，即求得单元格号
				Point.append(seq)
				temp[seq] = -1	#防止再次查找查过的元素
			sequenced_distance_matrix.append(Point)
		return sequenced_distance_matrix


"""
func：计算给定点集合的距离矩阵
"""
def cal_distance(points):
    distance_matrix = [[0.0]*len(points) for i in range(len(points))]
    for n, point1 in enumerate(points):
        for m, point2 in enumerate(points):
            dis = lambda x1, y1, x2, y2 : ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            distance_matrix[n][m] = dis(point1[0], point1[1], point2[0], point2[1])
    return distance_matrix

"""
func:计算路径长度
"""
def cal_distance(points):
		distance = 0
		for i, point in enumerate(points):
				if i < len(points) -1:
						distance += ( (points[i+1][0] - points[i][0])**2 + (points[i+1][1] - points[i][1] )**2  )**0.5
		return distance

"""
func:从文件获取遗传算法最短路径值
"""
def ga_distance():
		#读取文件
		f = open('ga.txt')
		pre = ''
		for line in f:
				if line != '':		#判断是否是最后一行
						pre = line
				else:
						pass
		parts = pre.split('\t')
		distance = (parts[-2])

		return distance
