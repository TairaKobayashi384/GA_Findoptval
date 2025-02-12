import random
import time

# Onemax問題の評価関数
def fitness(individual):
    result = 0
    # 10進数に変換
    for i in range(len(individual)): 
        result += ((1/2)**i) * individual[i] * 50

    return result

# 初期集団を生成
def create_population(pop_size, gene_length):
    return [[random.randint(0, 1) for _ in range(gene_length)] for _ in range(pop_size)]

# トーナメント選択（親選び）
def tournament_selection(population, fitness_scores, tournament_size=3):
    tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
    tournament.sort(key=lambda x: x[1], reverse=True)  # fitnessでソート
    return tournament[0][0]  # 最も良い個体を返す

# 交叉 (Crossover)
def singlepointcrossover(parent1, parent2, crossover_rate=0.7):
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)  # 交叉点
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        return child1, child2
    else:
        return parent1, parent2

# 交叉 (Crossover)
def twopointcrossover(parent1, parent2, crossover_rate=0.7):
    if random.random() < crossover_rate:
        (crossover_point0,crossover_point1) = sorted((random.randint(1, len(parent1) - 1),random.randint(1, len(parent1) - 1)))  # 交叉点
        child1 = parent1[:crossover_point0] + parent2[crossover_point0:crossover_point1] + parent1[crossover_point1:]
        child2 = parent2[:crossover_point0] + parent1[crossover_point0:crossover_point1] + parent2[crossover_point1:]

        return child1, child2
    else:
        return parent1, parent2
    
# 交叉 (Crossover)
def uniformcrossover(parent1, parent2, crossover_rate=0.7):
    child1,child2 = [],[]
    if random.random() < crossover_rate:
        for i in range(0,len(parent1)):
            if random.random() < 0.5:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child2.append(parent1[i])
                child1.append(parent2[i])
        return child1, child2
    else:
        return parent1, parent2

# 突然変異 (Mutation)
def mutate(individual, mutation_rate=0.01,indpb=0.01):
    if random.random() < mutation_rate:
        return [gene if random.random() > indpb else 1 - gene for gene in individual]
    
    return individual

# 遺伝的アルゴリズム
def genetic_algorithm(pop_size, gene_length, generations,crossover_rate=0.7, mutation_rate=0.01,indpb=0.01,tournsize=3,crossover='single'):
    start = time.time()

    # 初期集団を作成
    population = create_population(pop_size, gene_length)
    
    for generation in range(generations):
        # 各個体の適応度を計算
        fitness_scores = [fitness(individual) for individual in population]
        # 次世代を作成するための親選び
        new_population = []
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitness_scores,tournament_size=tournsize)
            parent2 = tournament_selection(population, fitness_scores,tournament_size=tournsize)
            
            # 交叉
            if(crossover==0):
                child1, child2 = singlepointcrossover(parent1, parent2, crossover_rate)
            elif(crossover==1):
                child1,child2 = twopointcrossover(parent1,parent2,crossover_rate)
            elif(crossover==2):
                child1,child2 = uniformcrossover(parent1,parent2,crossover_rate)
            
            # 突然変異
            child1 = mutate(child1, mutation_rate,indpb)
            child2 = mutate(child2, mutation_rate,indpb)
            
            # 新しい個体を追加
            new_population.append(child1)
            if len(new_population) < pop_size:
                new_population.append(child2)
        
        population = new_population
    
    # 最終世代の最良個体
    fitness_scores = [fitness(individual) for individual in population]
    best_individual = population[fitness_scores.index(max(fitness_scores))]

    end = time.time()

    return max(fitness_scores)-(end-start)
