best_individual = [36, 38, 40, 42, 44, 46, 47, 1, 0, 2, 4, 6, 8, 10, 12, 14, 16, 17, 15, 13, 11, 9, 7, 5, 3, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 18, 20, 22, 24, 26, 28, 30, 32, 34]
print([abs(best_individual[i+1]-best_individual[i]) for i in range(0,len(best_individual),2)])
