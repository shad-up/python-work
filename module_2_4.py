numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] == 1: continue
    for j in range(2, i):
        if numbers[i] % j == 0 and numbers[i] / j != 1:
            not_primes.append(numbers[i])
            break
    else:
        primes.append(numbers[i])
        continue
print(primes)
print(not_primes)