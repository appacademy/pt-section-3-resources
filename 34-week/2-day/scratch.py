# Dictionaries

# creating dictionaries
# customers = {
#     0: {"name": "Jason Lane"},
#     1: {"name": "Jesse Brooks"},
# }
# customers = dict(([{"name": "Jason Lane"}], [1, {"name": "Jesse Brooks"}]))
# print(customers)

# dictionary keys must be hashable (immutable)
# def name_printer(name):
#     print(name)

# random_data = {
#     # 1: "this key is a int",
#     "1": "this key is a string",
#     True: "this key is boolean",
#     (1,2): "this key is a tuple",
#     name_printer: "this key is a function",
# }
# print(random_data)
# print(random_data[(1,2)])
# print(random_data[name_printer])

# print(random_data[0])

# hashing
# print(hash((1,2)))
# print(hash((1,2)))
# print(hash(False))

customers = {
    0: {"name": "Jason Lane"},
    1: {"name": "Jesse Brooks"},
}

# accessing dictionaries
# print(customers[2])
# print(customers.get(2))

# adding to dictionaries
# customers[1] = {"name": "Henry Thompson"}
# customers.update(test={"name": "Henry"})

# print(customers)
# deleting from dictionaries
# del customers[2]
# print(customers)
# dictionary comprehensions

# key: value for element in iterable
# squares = {num: num*num for num in [1,2,3,4]}
# print(squares)

# sets

# creating sets
# even_nums = {2,4,6,8}
# even_nums = set([2,4,8,6])
# print(even_nums)

# set comprehensions
# return value for element in iterable if condition
# even_nums = {num for num in range(30) if num % 2 == 0}
# print(even_nums)


# set operations

# union | : takes the values of two sets and merges them into one set
# set_1 = {1,2,3,4}
# set_2 = {5,6,7,8}
# print(set_1 | set_2)

# intersection & : takes the values that are present in both sets
# set_1 = {5,6,3,4}
# set_2 = {5,6,7,8}
# print(set_1 & set_2)

# difference - : what values are in set a, that are not in set b?
# set_1 = {5,6,3,4}
# set_2 = {5,6,7,8}
# print(set_1 - set_2)
# print(set_2 - set_1)
# symmetric difference ^ : what values are not common/intersected in both sets
# set_1 = {1,2,3,4,9}
# set_2 = {5,6,7,8,9}
# print(set_1 ^ set_2)
