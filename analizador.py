from neat import config, population, chromosome, genome, visualize
from neat.nn import nn_pure as nn
from checkpoint import Checkpointer
from player_2048 import *

import sys

pop = Checkpointer.restore_checkpoint(sys.argv[1])

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