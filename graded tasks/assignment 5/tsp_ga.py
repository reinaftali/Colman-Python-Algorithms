import random
import math

def solve(points):
    population_size = 100
    generations = 500
    mutation_rate = 0.01
    tournament_size = 5

    population = [random.sample(points, len(points)) for _ in range(population_size)]

    for generation in range(generations):
        fitness_scores = [fitness(individual) for individual in population]
        selected_population = selection(population, fitness_scores, tournament_size)
        next_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover(parent1, parent2)
            next_population.extend([child1, child2])
        population = [mutate(individual, mutation_rate) for individual in next_population]

    best_individual = min(population, key=fitness)
    return best_individual

def dist(p1, p2):
    return float(math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2))

def fitness(points):
    return sum(dist(points[i - 1], points[i]) for i in range(1, len(points))) + dist(points[-1], points[0])

def selection(population, fitness_scores, tournament_size):
    selected_population = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
        winner = min(tournament, key=lambda x: x[1])
        selected_population.append(winner[0])
    return selected_population

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child1, child2 = [None] * len(parent1), [None] * len(parent1)
    child1[start:end], child2[start:end] = parent1[start:end], parent2[start:end]
    fill_child(child1, parent2, start, end)
    fill_child(child2, parent1, start, end)
    return child1, child2

def fill_child(child, parent, start, end):
    current_pos = end
    for gene in parent:
        if gene not in child:
            if current_pos >= len(parent):
                current_pos = 0
            child[current_pos] = gene
            current_pos += 1

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual
