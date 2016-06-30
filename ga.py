import copy
import random
import single_nao_control

class Individual(object):
  def __init__(self, chromosome, fitness):
    self.chromosome = chromosome
    self.fitness = fitness

class GeneticAlgorithm(object):
  def __init__(self, chromosomeSize, populationSize, numberOfGenerations, mutants, elite, probElite, probMut):
    self.populationSize = populationSize
    self.numberOfGenerations = numberOfGenerations
    self.mutants = mutants
    self.elite = elite
    self.chromosomeSize = chromosomeSize
    self.probElite = probElite
    self.probMut = probMut
    self.currentGeneration = 0
    self.population = []
    self.initPopulation()

  def initPopulation(self):
    i = 0
    while i < self.populationSize:
      x = []
      j = 0
      while j < self.chromosomeSize:
        x.append(random.uniform(0.0, 1.0))
        j += 1
      self.population.append(Individual(x, self.calculateFitness(x)))
      i += 1
    self.population.sort(key = lambda x: x.fitness, reverse = True)

  def calculateFitness(self, chromosome):
    # Implement fitness function
    print chromosome
    fit = single_nao_control.runSimulation([chromosome])
    print 'fitness:'
    print fit[0]
    print 'pos x:'
    print fit[1]
    return fit[0]
    #return random.randint(0, 10)

  def start(self):
    while self.currentGeneration < self.numberOfGenerations:
      print "Geracao atual"
      print self.currentGeneration
      self.getNextPopulation()
      self.currentGeneration += 1

  def getNextPopulation(self):
    nextPopulation = copy.deepcopy(self.population)
    i = self.elite
    while i < self.populationSize - self.mutants:
      # Crossover
      elite_parent = random.randint(0, self.elite - 1)
      normal_parent = random.randint(self.elite, self.populationSize - 1)
      j = 0
      while j < self.chromosomeSize:
        parent = elite_parent if random.uniform(0.0, 1.0) < self.probElite else normal_parent
        nextPopulation[i].chromosome[j] = self.population[parent].chromosome[j]
        j += 1
      nextPopulation[i].fitness = self.calculateFitness(nextPopulation[i].chromosome)
      i += 1
    while i < self.populationSize:
      j = 0
      while j < self.chromosomeSize:
        # Mutation
        nextPopulation[i].chromosome[j] = random.uniform(0.0, 1.0) if random.uniform(0.0, 1.0) < self.probMut else nextPopulation[i].chromosome[j]
        j += 1
      nextPopulation[i].fitness = self.calculateFitness(nextPopulation[i].chromosome)
      i += 1
    self.population = copy.deepcopy(nextPopulation)
    self.population.sort(key = lambda x: x.fitness, reverse = True)

  def getBestIndividual(self):
    return self.population[0].chromosome

  def debug(self):
    print("Population", [(x.fitness, x.chromosome) for x in self.population])

def main():
  # Chromosome Size
  # Population Size
  # Number Of Generations
  # Number Of Mutants
  # Number of Elite Individuals
  # Probability oO Inheriting From An Elite Parent
  # Probability Of Mutation
  ga = GeneticAlgorithm(2, 5, 15, 2, 2, 0.7, 0.3)
  ga.debug()
  ga.start()
  ga.debug()
  print(ga.getBestIndividual())

if __name__ == "__main__":
  main()
