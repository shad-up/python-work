tir = []
tir2 = []
for i in range(20):
    tir.append(i+1)
    tir2.append(i+1)
result = []
n = int(input('Введите число от 3 до 20 '))
for j in range(len(tir)):
    one = tir[j]
    tir2.remove(tir[j])
    for l in range(len(tir2)):
        two = tir2[l]
        summa = one + two
        #print(summa)
        if n % summa == 0:
            result.append([one, two])
print(result)




