# tsp_ga_greedy_python
该项目使用了python3.x，解决了无人机如何遍历不规则的问题

核心算法：贪心算法、遗传算法
	当然，贪心算法是自己实现的，而遗传算法则是使用现成的库deap，有兴趣的童鞋可以搜搜



文件功能 介绍：
	algorithms.py————解决TSP问题的几种算法
	common.py————常用来计算的一些函数，例如求点集的距离矩阵
	create.py————创建指定节点数目的函数，并存储到指定文件points.json中
	figure.py————封装了一些常用的作图函数
	ga_init.py————遗传算法之前的准备，由于使用了现有的进化算法库deap，个人需要修改其中的功能，所以在这个文件中进行了适当修改
	ga_optimize_cross_rate————对遗传算法中的交叉率参数进行优化
	ga_optimize_population_size————对遗传算法中的种群数量参数进行优化
	ga_optimize_mutation_rate————对遗传算法中的基因突变参数进行优化
	ga_optimize_evolution_gens————对遗传算法中的繁殖代数参数进行优化
	four_algorithms_compared————两种算法的四种组合的对比（**运行时间好几个小时，也可以适当修改节点数目，以节约时间**）
	init.py——基本的操作，处理点集，读取文件等等
