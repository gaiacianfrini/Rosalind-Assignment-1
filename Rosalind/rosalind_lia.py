from math import comb

def probability_k_generation(k, N):
    total_population = 2 ** k
    prob_AaBb = 1/4  # Probability that an organism has genotype Aa Bb
    probability = 0
    
    for x in range(N):
        probability += comb(total_population, x) * (prob_AaBb ** x) * ((1 - prob_AaBb) ** (total_population - x))
    
    return 1 - probability

k = 5  # Example value for k
N = 8  # Example value for N
result = probability_k_generation(k, N)
print(result)



