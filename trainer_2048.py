from player_2048 import *
from neat import config, population, chromosome, genome, visualize
from neat.nn import nn_pure as nn

config.load('2048_config')

max_generations = 1000

# set node gene type
chromosome.node_gene_type = genome.NodeGene

# XOR-2
#INPUTS = [[0, 0], [0, 1], [1, 0], [1, 1]]
#OUTPUTS = [0, 1, 1, 0]

def eval_fitness(population):

    #global melhor_score

    for chromo in population:
        net = nn.create_ffphenotype(chromo)

        #error = 0.0
        #error_stanley = 0.0
        #for i, inputs in enumerate(INPUTS):
        #net.flush() # not strictly necessary in feedforward nets

        score = play_with_AI(net)

        #if score > melhor_score:
        #    melhor_score = score

        #print 'Melhor: ------------- ' + str(int(melhor_score))

        #print 'olha esse score:'
        #print score


        #output = net.sactivate(inputs) # serial activation
        #error += (output[0] - OUTPUTS[i])**2

        #error_stanley += math.fabs(output[0] - OUTPUTS[i])

        #chromo.fitness = (4.0 - error_stanley)**2 # (Stanley p. 43)
        #chromo.fitness = 1 - math.sqrt(error/len(OUTPUTS))
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