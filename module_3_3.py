def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)

print_params()
print_params(2)
print_params(2, 'тест')
print_params(3, 'еще_тест', False)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'еще_строка', False]
print_params(*values_list)

values_dict = {'a': 13.37, 'b': 'строкаааа', 'c': [2,2,8]}
print_params(**values_dict)

values_list2 = [1.2, 'опять_строка']
print_params(*values_list2, 42)
