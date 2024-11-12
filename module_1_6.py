my_dict = {'Anna': 2000, 'Boris': 1956, 'Leto': 1978, 'Rita': 2002}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Roma'))
my_dict.update({'Roma': 2005, 'Gad': 2008})
a = my_dict.pop('Gad')
print(a)
print(my_dict)
my_set = {1, 2, 3, 5, 3, 'w', 's', 4, 's', 1}
print(my_set)
my_set.add(6)
my_set.add(7)
my_set.remove('w')
print(my_set)