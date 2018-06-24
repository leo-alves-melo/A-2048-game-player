from player_2048 import *
from neat import config, population, chromosome, genome, visualize
from neat.nn import nn_pure as nn

config.load('2048_config')

max_generations = 1000

# set node gene type
chromosome.node_gene_type = genome.NodeGene

def eval_fitness(population):

	#global melhor_score

	for chromo in population:
		net = nn.create_ffphenotype(chromo)

		score = play_with_AI(net)
		chromo.fitness = score

population.Population.evaluate = eval_fitness

pop = population.Population()
pop.epoch(max_generations, report=True, save_best=False)

winner = pop.stats[0][-1]
print('Number of evaluations: %d' %winner.id)

# Visualize the winner network (requires PyDot)
visualize.draw_net(winner) # best chromosome

# Plots the evolution of the best/average fitness (requires Biggles)
visualize.plot_stats(pop.stats)
# Visualizes speciation
visualize.plot_species(pop.species_log)

# Let's check if it's really solved the problem
print('\nBest network output:')
brain = nn.create_ffphenotype(winner)
score = play_with_AI(brain)
print 'score do melhor: ' + str(int(score))