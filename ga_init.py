import array
import random
import numpy


from deap import base
from deap import creator
from deap import tools

#自定义模块
import common


def varAnd(population, toolbox, cxpb, mutpb):
    offspring = [toolbox.clone(ind) for ind in population]

    # Apply crossover and mutation on the offspring
    for i in range(1, len(offspring), 2):
        if random.random() < cxpb:
            offspring[i-1], offspring[i] = toolbox.mate(offspring[i-1], offspring[i])
            del offspring[i-1].fitness.values, offspring[i].fitness.values

    for i in range(len(offspring)):
        if random.random() < mutpb:
            offspring[i], = toolbox.mutate(offspring[i])
            del offspring[i].fitness.values

    return offspring

def eaSimple(population, toolbox, cxpb, mutpb, ngen, stats=None,
             halloffame=None, verbose=__debug__):
    logbook = tools.Logbook()
    logbook.header = ['gen', 'nevals'] + (stats.fields if stats else [])

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in population if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    #得到最初的适应值
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    if halloffame is not None:
        halloffame.update(population)

    #record 存储的是std、max、vag、min
    record = stats.compile(population) if stats else {}
	#kog.record 存储的是std、gen、nevals、min、avg、max
    logbook.record(gen=0, nevals=len(invalid_ind), **record)
    if verbose:
        pass
        #print(logbook.stream)
	#开始进化 
    for gen in range(1, ngen+1):
        # Select the next generation individuals
        offspring = toolbox.select(population, len(population))

		# Vary the pool of individuals
        offspring = varAnd(offspring, toolbox, cxpb, mutpb)

		#print(offspring)
		# Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

		# Update the hall of fame with the generated individuals
        if halloffame is not None:
            halloffame.update(offspring)

		# Replace the current population by the offspring
        population[:] = offspring

		# Append the current generation statistics to the logbook
        record = stats.compile(population) if stats else {}
        logbook.record(gen=gen, nevals=len(invalid_ind), **record)
        if verbose:
            pass
            #print(logbook.stream)
    return population, logbook, ind

"""
func:遗传算法具体实施
"""
def ga(points, start_point, population_size, cross_rate, mutation_rate, gens):
		all_points = [start_point] + points
		IND_SIZE = len(all_points)
		distance_matrix = common.cal_distance_matrix(all_points)


		"""
		func:求每一种飞行测略的路径长度
		"""
		def evalTSP(individual):
				distance = 0
				#distance = distance_matrix[individual[-1]][individual[0]]
				for gene1, gene2 in zip(individual[0:-1], individual[1:]):
					distance += distance_matrix[gene1][gene2]
				return distance,

		#算法基本准备
		creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
		creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

		toolbox = base.Toolbox()

		#个体生成器——随机产生个体
		toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)
		toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
		toolbox.register("population", tools.initRepeat, list, toolbox.individual)

		#交叉配对、基因突变、选择、进化
		toolbox.register("mate", tools.cxPartialyMatched)
		toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
		toolbox.register("select", tools.selTournament, tournsize=3)
		toolbox.register("evaluate", evalTSP)

		random.seed(169)
		pop = toolbox.population(population_size)
		hof = tools.HallOfFame(1)
		stats = tools.Statistics(lambda ind: ind.fitness.values)
		stats.register("avg", numpy.mean)
		stats.register("std", numpy.std)
		stats.register("min", numpy.min)
		stats.register("max", numpy.max)

		#ind为路径序号
		population, distances, route = eaSimple(pop, toolbox, cross_rate, mutation_rate, gens, stats=stats, halloffame=hof)

		return population, distances, route


