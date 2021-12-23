from collections import Counter
with open('Dec6/Dec6-data.txt') as f:
    inp = list(map(lambda x: int(x), f.read().split(",")))
population = dict((_, 0) for _ in range(9))
population.update(dict(Counter(inp)))
for i in range(256):
    newPopulation = dict((_, 0) for _ in range(9))
    for _ in range(8):
        newPopulation[_] = population[_ + 1]
    newPopulation[6] += population[0]
    newPopulation[8] = population[0]
    population = newPopulation
values = population.values()
print(sum(values))
