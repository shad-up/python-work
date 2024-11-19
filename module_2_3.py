my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
s = 0
f = len(my_list) + 1
while s != f:
    if my_list [s] == 0:
        s = s + 1
        continue
    elif my_list [s] > 0:
        print(my_list [s])
        s = s + 1
    elif my_list [s] < 0:
        break