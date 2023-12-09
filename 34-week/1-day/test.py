# def my_func(score):
#     score = 5
#     return score >= 90

# only_as = filter(my_func, scores)

# # only_as = filter(lambda el: el >= 90, scores)
# # only_as = filter(lambda el: el >= 90, scores)
# # only_as = filter(lambda el: el >= 90, scores)
# # only_as = filter(lambda el: el >= 90, scores)


# print("2: ", list(only_as))
# #


# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# strings_list = ["b", "a", "k", "c", "d", "e", "m"]

# print(scores.sort())
# print(scores)
# strings_list.sort(reverse=True)

# DAYS = ("MON", "TUE", "WED", "THUR", "FRI")


# def my_sort_func(el):
#     print("in func:", el)

#     return "hello"

# # num_list = [20, 3, 5, 2, 1, 4]
# # num_list = [3, 5, 2, 20, 4]
# # some_dict = {"a": 1, "b": 2, "c": 3}
# # [20, 2, 4]
# # [3, 5, 1]

# sorted_nums = sorted(some_dict, key=my_sort_func)
# # sorted_nums = sorted(num_list)
# print("\nNew List:", sorted_nums)


# new_days = sorted(DAYS)

# print("2: ", new_scores)


# print(strings_list)


# def my_kwarg_func(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])
#     # print("name:", name, "\nage:", age, "\nreverse:", reverse)

#     # return "Hello world"

# my_kwarg_func(age=50, name="will", reverse=True)


# DAYS = ("MON", "TUE", "WED", "THUR", "FRI")
# vals = [5, 4, 3, 2, 1]
# def my_func(el):
#     print("in func:", el)
#     return el * 2


# map_list = map(my_func, my_list)
# # map_list2 = map(my_func, my_list)
# print("1: ", map_list)
# # print("1: ", map_list2)

# dog = map_list
# print("DOG", dog)


# my_list1 = [5, 6, 7, 8, 9]
# my_list2 = [100, 1_000, 10_000, 100_000, 1_000_000]

# for index, x in enumerate(my_list1):
#     print(index, x)



# my_list = [1,2,3]

# map_list = list(map(lambda el: el * 2, my_list))

# print("1: ", map_list)

# def my_sort_func(el1, el2):
#     print("in func:", el1, "\nel2:", el2)
#     return "hello"


# sorted_nums = map(my_sort_func, list(enumerate(my_list1)), list(enumerate(my_list2)))

# print("2: ", list(sorted_nums))

# enum_list = enumerate(my_list)
# print("Enum list: ", list(enum_list))

# for index, el in enumerate(my_list):
#     print(index, el)

# some_dict = {"b": 1, "a": 2, "c": 3}
# # print(list(enumerate(some_dict)))
# for key, val in some_dict.items():
#     print(key, val)
