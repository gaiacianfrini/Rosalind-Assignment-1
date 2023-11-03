#Rosalind FIB
def rabbit_pairs(n, k):
    starting_rabbits = [1,1]
    for i in range (2, n+1):
        next_rabbits = starting_rabbits[i-1] + k * starting_rabbits[i-2]
        starting_rabbits.append(next_rabbits)
    return starting_rabbits[n - 1]

n = 29
k = 3
result = rabbit_pairs(n, k)
print(result)