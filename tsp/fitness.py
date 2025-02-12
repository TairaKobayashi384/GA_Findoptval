import random
import matplotlib.pyplot as plt
import statistics
import csv
import math
import time

#DNA_LENの数の街を作成

#町を生成する関数(今回は同心円状にランダムではなくC型、歯車型の二種類をランダムに生成)
def make_cities(cities_num,radius_ratio=1):
    cities = []
    for i in range(0,cities_num):
        #外円を描画
        cities.append((math.cos(math.radians((i/cities_num)*360)),math.sin(math.radians((i/cities_num)*360))))
        #内円を描画
        cities.append((radius_ratio*math.cos(math.radians((i/cities_num)*360)),radius_ratio*math.sin(math.radians((i/cities_num)*360))))

    return cities

#距離の最適解を求める関数
def getoptimaldistance(cities_num,radius_ratio):
    #外側の多角形の一辺の大きさ
    outercircle = math.sin(math.radians(360/cities_num))
    #内側の多角形の一辺の大きさ
    innercircle = math.sin(math.radians(360/cities_num))*radius_ratio

    if(radius_ratio < 0.76908):
        #C型
        d = outercircle*(cities_num/2-1)+innercircle*(cities_num/2-1)+2*(1-radius_ratio)
    else:
        #歯車型
        d = (1-radius_ratio)*(cities_num/2)+(innercircle)*(cities_num/2)+(outercircle)*(cities_num/2)

    return d

#city1とcity２の座標を受け取って距離を返す関数
def distance(city1,city2):
    return ((city1[0]-city2[0])**2+(city1[1]-city2[1])**2)**0.5

#評価関数
def fitness(cities,individual):
    total_distance = 0

    for i in range(len(individual)-1):
        total_distance += distance(cities[individual[i]],cities[individual[i+1]])

    #最後の都市から最初の都市に移動するまでの距離
    total_distance += distance(cities[individual[-1]],cities[individual[0]])

    return total_distance

def create_population(pop_size,gene_length):
    # ルートを作る
    route = [i for i in range(gene_length)]
    random.shuffle(route)
    
    return [[_ for _ in route] for _ in range(pop_size)]

def tournament_selection(population,fitness_scores,tournament_size=3):
    tournament = random.sample(list(zip(population,fitness_scores)), tournament_size)
    tournament.sort(key=lambda x: x[1])
    return tournament[0][0]

def crossover(parent1,parent2,crossover_rate=0.7):
    if random.random() < crossover_rate:
        genelen = len(parent1)

        child1,child2 = [-1 for i in range(genelen)],[-1 for i in range(genelen)]

        #２つの部分を決める
        start,end = sorted(random.sample(range(genelen),2))

        #child1 ではparent1からそのまま遺伝子を取り、child2 ではparent２からそのまま遺伝子を受け取る
        child1[start:end+1] = parent1[start:end+1]
        child2[start:end+1] = parent2[start:end+1]

        #残りの部分を埋める
        for i in range(genelen):
            # child1はparent2から埋める
            if child1[i] == -1:
                for gene in parent2:
                    if gene not in child1:
                        child1[i] = gene

            # child1はparent2から埋める
            if child2[i] == -1:
                for gene in parent1:
                    if gene not in child2:
                        child2[i] = gene

        return child1,child2

    else:
        return parent1,parent2
    
def mutate(individual,mutation_rate=0.01,indpb=0.01):
    size = len(individual)
    
    if(random.random() < mutation_rate):
        # 入れ替える
        for i in range(size):
            if(random.random() < indpb):
                change_gene1,change_gene2 = sorted(random.sample(range(size),2))

                individual[change_gene1],individual[change_gene2] = individual[change_gene2],individual[change_gene1]

    return individual

# 遺伝的アルゴリズム
def genetic_algorithm(pop_size, gene_length, generations,crossover_rate=0.7, mutation_rate=0.01,indpb=0.01,tournsize=3):
    radius_ratio = random.random()

    optimald = getoptimaldistance(len(cities)*2,radius_ratio)

    cities = make_cities(gene_length,radius_ratio)

    # 初期集団を作成
    population = create_population(pop_size, gene_length)
    
    for generation in range(generations):
        # 各個体の適応度を計算
        fitness_scores = [fitness(cities,individual)/optimald for individual in population]
        # 最良の個体を表示
        best_individual = population[fitness_scores.index(min(fitness_scores))]
        print(f"Generation {generation} - Best fitness: {min(fitness_scores)} - Best individual: {best_individual}")
        fitness(cities,best_individual)


        # 次世代を作成するための親選び
        new_population = []
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitness_scores,tournament_size=tournsize)
            parent2 = tournament_selection(population, fitness_scores)
            
            # 交叉
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            
            # 突然変異
            child1 = mutate(child1, mutation_rate,indpb)
            child2 = mutate(child2, mutation_rate,indpb)
            
            # 新しい個体を追加
            new_population.append(child1)
            if len(new_population) < pop_size:
                new_population.append(child2)
        
        population = new_population
    
    # 最終世代の最良個体
    fitness_scores = [fitness(cities,individual) for individual in population]
    best_individual = population[fitness_scores.index(min(fitness_scores))]

    print(f"Final Best fitness: {min(fitness_scores)} - Best individual: {best_individual}")

    print([best_individual[i]-best_individual[i+1] for i in range(len(best_individual))])

if __name__ == "__main__":
    pop_size = 100  # 集団サイズ
    gene_length = 100  # 遺伝子の長さ(= 町の数)
    generations = 10000  # 世代数

    # これをoutputする
    genetic_algorithm(pop_size, gene_length, generations)
