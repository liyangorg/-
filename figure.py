import matplotlib.pyplot as plt
from  matplotlib.patches import Rectangle

"""
功能：设置图像的坐标轴和网格的样式
"""
def set_axes_grid():
		major_axis = 10
		minor_axis = 2
		ax =plt.axes()
		ax.set_xlim(0,100)
		ax.set_ylim(0,100)
		ax.xaxis.set_major_locator(plt.MultipleLocator(major_axis))
		ax.xaxis.set_minor_locator(plt.MultipleLocator(minor_axis))
		ax.yaxis.set_major_locator(plt.MultipleLocator(major_axis))
		ax.yaxis.set_minor_locator(plt.MultipleLocator(minor_axis))

		ax.grid(which='major', axis='x', linewidth='0.75', linestyle=':', color='0.75')
		ax.grid(which='minor', axis='x', linewidth='0.25', linestyle='-', color='0.75')
		ax.grid(which='major', axis='y', linewidth='0.75', linestyle=':', color='0.75')
		ax.grid(which='minor', axis='y', linewidth='0.25', linestyle='-', color='0.75')

"""
功能：绘制存在点的单元格--阴影覆盖
args：
	units：需要覆盖的单元格坐标
	ax：图像参数
"""
def fill_cell(cell_info, ax):
	#获取cell中心坐标集合cells
	cells = [[0,0]]*len(cell_info)
	for i, val in enumerate(cell_info):
		cells[val] = cell_info[val]

	#填充单元格内部
	for i, val in enumerate(cells):
			ax.add_patch(Rectangle(((val[0]-5), (val[1]-5)),10,10,alpha=0.2))

"""
func:根据给定的route画出路线规划图
"""
def paint_route(route):
		set_axes_grid()
		rx = []
		ry = []
		for i, point in enumerate(route):
				rx.append(point[0])
				ry.append(point[1])
		plt.plot(rx, ry, color='r')
		plt.show()

"""
func：绘制程序图形总函数
"""
#def paint
