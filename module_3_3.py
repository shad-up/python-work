def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(1,2)
print_params((1,2.3), 'bum', False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [88, 'badabum', True]
values_dict = {'a': 1, 'b': (3, 5, 7), 'c': 'loc'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ('aga', 9)
print_params(*values_list_2, 42)