import numpy as np

class genetic_algorithm():
    def __init__(self):
        self.population = None
        self.best_score = 0
        self.attributes = []
        self.value = []
        self.weight = []
        self.limit = 0

    def add_attributes(self, attributes):
        for attr in attributes:
            self.attributes.append(attr)
        self.value = np.array(self.attributes)[:,0]
        self.weight = np.array(self.attributes)[:,1]

    def initiate_pop(self, pop_size):
        self.population = np.round(np.random.random((pop_size, len(self.attributes))))

    def fitness(self, pop):
        if np.sum(pop*self.weight) <= self.limit:
            return np.sum(pop*self.value)
        else:
            return 0

    def survive(self, survivor_amount):
        scores = []
        survivors = []
        for pop in self.population:
            scores.append(self.fitness(pop))
        for _ in range(survivor_amount):
            survivors.append(self.population[np.argmax(scores)])
            scores[np.argmax(scores)] = -1
        return survivors

    def intercourse(self):
        children = []
        daddy = None
        mommy = None
        survivors = self.survive(len(self.value)//2)
        apex = survivors[:2]
        self.population = np.random.shuffle(survivors)
        for survivor in survivors:
            if daddy is None:
                daddy = list(survivor)
            else:
                mommy = list(survivor)
                children.append(daddy[:2] + (mommy[2:]))
                children.append(mommy[:2] + (daddy[2:]))
                daddy = None
        self.population = children
        return apex

    def evolve(self, evolutions, limit):
        self.limit = limit
        for i in range(evolutions):
            apex = self.intercourse()
            print("\nGeneration ", i+1, " :")
            for ape in apex:
                print("Gene Code: ", ape)
                print("Fitness", self.fitness(ape))


gen = genetic_algorithm()

attributes = [[5, 7], [3, 1], [5, 5], [12, 4]]

gen.add_attributes(attributes)
gen.initiate_pop(10)
gen.evolve(100, 10)