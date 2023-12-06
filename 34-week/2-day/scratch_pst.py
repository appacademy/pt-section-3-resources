# Dictionaries


# creating dictionaries
# customers = {
#     0: {
#         "name": "Jesse",
#         "age": 27
#     },
#     1: {
#         "name": "Edward",
#         "age": 25
#     }
# }

# customers_2 = dict(
#     [
#         (0, {"name": "Jesse", "age": 27}),
#         (1, {"name": "Edward", "age": 25}),
#         [2, {"name": "Cliff Edwards", "age": 32}],
#         [1]
#     ]
# )

# print(customers)
# print(customers_2)

# hashing

# def name_printer(name):
#     print(name)

# random_data = {
#     # 0: "this key is an int",
#     "1": "this key is a string",
#     True: "this key is a boolean",
#     (1,2): "this key is a tuple",
#     name_printer: "this key is a function",
#     # [1,2,3]: "this key is supposed to be a list"
# }

# print(random_data)

# accessing dictionaries
# print(random_data[0])
# print(random_data[1])
# print(random_data[True])
# print(random_data[(1,2)])
# print(random_data[name_printer])

# print(hash(1))
# print(hash(True))
# print(hash((1,2,3)))
# print(hash((1,2)))
# print(hash([]))

# print(random_data[0])
# print(random_data.get(0))

# customers = {
#     0: {
#         "name": "Jesse",
#         "age": 27
#     },
#     1: {
#         "name": "Edward",
#         "age": 25
#     }
# }
# adding to dictionaries
# print(customers)
# customers[2] = {"name": "John Smit", "age": 38}
# print(customers)
# customers[0] = {
#         "name": "Jesse Brooks",
#         "age": 27
# },
# print(customers)

# deleting from dictionaries
# print(customers)
# del customers[0]
# print(customers)

# dictionary comprehensions
# key: value for element in iterable
# squares = {num: num * num for num in (1,2,3,4,5)}
# print(squares)

# sets

# creating sets
# even_nums = {2,4,6,8,10,12}
# odd_nums = set([1,3,5,7,9,12])
# print(even_nums)
# print(odd_nums)

# set comprehensions
# even_nums = {num for num in range(30) if num % 2 == 0}
# print(even_nums)

# set operations

# union | : takes the values of two sets and merges them into one set
# print(even_nums | odd_nums)

# intersection & : takes the values that are present in both sets
# print(even_nums & odd_nums)

# difference - : what values are in set a, that are not in set b?
# print(even_nums - odd_nums)

# symmetric difference ^ : what values are not common/intersected in both sets
# print(even_nums ^ odd_nums)
