def calculate_structure_sum(*args):
    total = 0
    for data in args:
        if isinstance(data, (int, float)):
            total += data
        elif isinstance(data, str):
            total += len(data)
        elif isinstance(data, (list, tuple, set)):
            total += calculate_structure_sum(*data)
        elif isinstance(data, dict):
            total += calculate_structure_sum(*data.items())
    return total

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)