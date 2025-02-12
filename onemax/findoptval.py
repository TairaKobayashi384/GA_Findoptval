import random
import fitness as fit

MAX_POP = 100
GENES = 100
MAX_GENERATIONS = 100
MAX_CXRATE = 1
MAX_MURATE =1
MAX_CROSSOVER = 2

# Onemax問題の評価関数
def fitness(individual):
    #1の数をカウント
    return fit.genetic_algorithm(individual[0],individual[1],individual[2],individual[3],individual[4],individual[5],individual[6],individual[7])

# 初期集団を生成
def create_population(pop_size):
    pops = []
    for i in range(pop_size):
        pop = []
        #pop
        pop.append(random.randint(10,MAX_POP))
        #genes
        pop.append(GENES)
        #gen
        pop.append(random.randint(10,MAX_GENERATIONS))    
        #cxrate
        pop.append(random.random())
        #mutpb
        pop.append(random.random())
        #indpb
        pop.append(random.random())
        #TOURNSIZE <= MAX_POP
        pop.append(random.randint(1,pop[0]))
        pop.append(random.randint(0,MAX_CROSSOVER))

        pops.append(pop)

    return pops

# トーナメント選択（親選び）
def tournament_selection(population, fitness_scores, tournament_size=3):
    tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
    tournament.sort(key=lambda x: x[1], reverse=True)  # fitnessでソート
    return tournament[0][0]  # 最も良い個体を返す

# 交叉 (Crossover)
def crossover(parent1, parent2, crossover_rate=0.7):
    child1,child2 = [],[]
    if random.random() < crossover_rate:
        for i in range(0,len(parent1)):
            if random.random() < 0.5:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])

        #トーナメント>人数になってしまうことを避ける。
        if(child1[6] > child1[0] or child2[6] > child2[0]):
            #親1、親2のどっちかだからこうして問題はなし
            child1[6],child2[6] = child2[6],child1[6]

        return child1, child2
    else:
        return parent1, parent2

# 突然変異 (Mutation)

# 突然変異 (Mutation)
def mutate(individual, mutation_rate=0.01):
    individual_tmp = []

    for i in range(len(individual)):
        if(random.random() < mutation_rate):
            #pop
            if(i == 0):
                individual_tmp.append(random.randint(1,MAX_POP))
                continue
            #genes
            elif(i == 1):
                individual_tmp.append(GENES)
                continue
            #gen
            elif(i == 2):
                individual_tmp.append(random.randint(1,MAX_GENERATIONS))
                continue 
            #cxrate
            elif(i == 3):
                individual_tmp.append(random.random())
                continue
            #mutrate
            elif(i == 4):
                individual_tmp.append(random.random())
                continue
            #indpb
            elif(i == 5):
                individual_tmp.append(random.random())
                continue
            #tournsize
            elif(i == 6):
                individual_tmp.append(random.randint(1,individual_tmp[0]))
                continue
            #crossover
            elif(i == 7):
                individual_tmp.append(random.randint(0,MAX_CROSSOVER))
                continue
        else:
            individual_tmp.append(individual[i])

    #tournsizeだけindividualの設定が引き継がれて、POPが少なくなってしまった場合は再度tournsizeを設定する
    if(individual_tmp[6] > individual_tmp[0]):
        individual_tmp[6] = random.randint(1,individual_tmp[0])

    return individual_tmp

# 遺伝的アルゴリズム
def genetic_algorithm(pop_size, generations,crossover_rate=0.7,mutation_rate=0.01,tournsize=3):
    # 初期集団を作成
    population = create_population(pop_size)
    
    for generation in range(generations):
        # 各個体の適応度を計算
        fitness_scores = [fitness(individual) for individual in population]

        # 最良の個体を表示
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        print(f"Generation {generation} - Best fitness: {max(fitness_scores)} - Best individual: {best_individual}")

        # 次世代を作成するための親選び
        new_population = []
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitness_scores,tournament_size=tournsize)
            parent2 = tournament_selection(population, fitness_scores,tournament_size=tournsize)
            
            child1,child2 = crossover(parent1,parent2,crossover_rate)

            # 突然変異
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            
            # 新しい個体を追加
            new_population.append(child1)
            if len(new_population) < pop_size:
                new_population.append(child2)
        
        population = new_population
    
    # 最終世代の最良個体
    fitness_scores = [fitness(individual) for individual in population]
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    print(f"Final Best fitness: {max(fitness_scores)} - Best individual: {best_individual}")


    return max(fitness_scores)

if __name__ == '__main__':
    GENES = 100
    genetic_algorithm(100,1000)
    
    #for i in range(1,100):
    #    GENES = i * 10
    #    genetic_algorithm(100,500)