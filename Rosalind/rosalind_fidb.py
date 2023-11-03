def mortal_fibonacci(n, m): 
    pairs = [1, 1] #initial pairs and its offspring in the second month
    for i in range(2, n):
        # first reproduction
        population = pairs[i - 1] + pairs[i - 2]
        # then death
        if i == m:
            population = population - 1
        if i > m:
            population = population - pairs[i - m - 1]
        pairs.append(population)
    return pairs[-1]

n = 93 # months
m = 16 # survival time

print(mortal_fibonacci(n, m))
