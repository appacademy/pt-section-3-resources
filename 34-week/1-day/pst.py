# def my_func():
#     print("Hello world")
# my_func()



# my_tuple = (1,2,3,4)
# print("my_tuple:", my_tuple)

# for x in my_list:
#     print(x)

# for x in my_tuple:
#     print(x)




# my_list = ["taco", 2, 3, 4]
# my_iter = iter(my_list)
# try:
#     print("my_iter:", next(my_iter))
#     print("my_iter:", next(my_iter))
#     print("my_iter:", next(my_iter))
#     print("my_iter:", next(my_iter))
#     print("my_iter:", next(my_iter))
# except:
#     print("ERROR: No more elements in iterator")



# my_list = [1,2,3,4,5]


# print("1: ", list(filtered_list))



# my_list = [3,6,8,2,4]
# my_tuple = (3,6,8,2,4)

# # # filtered_list1 = filter(lambda x: x > 2, my_list)
# filtered_list2 = filter(lambda x: x > 2, my_list)

# print("1: ", filtered_list2)



# print("1: ", list(filtered_list1))
# print("1: ", list(filtered_list2))

# new_variable = filtered_list
# print("2: ", new_variable)

# whatever_it_evaluates_to = my_list.sort()
# print("\nmy_list: ", sorted_list)
# print("my_list: ", my_list)
# print("sort: ", my_list)



# print("my_list: ", my_list[0])

# for x in my_list:
#     print(x)

# my_list = [3,6,7,4]

# def my_custom_func(x):
#     print("X: ", x, "\nx mod 2:", x % 2)
#     return x % 2

# sorted_list = sorted(my_list)

# print("sorted: ", sorted_list)



# def my_func(**kwargs):
#     print("kwargs:", kwargs)

# my_func(name="bob", age=30, reverse=True, height=5.5)

# my_list = [1,2,3]

# def my_func(name, first_num, *args, **kwargs):
#     print("name:", name)
#     print("first_num:", first_num)
#     print("args:", args)

# my_func("will", "bob", 1,2,3,4, "hello", [1,2,3], {"name": "bob"})



# print("old list: ", my_list)
# print("mapped_list: ", mapped_list)
# # print(tuple(map_obj))


# Any and All
# test = ["item", [], []]
# # test = [True, False, True]
# print("Any:", any(test))
# print("\nAll:", all(test))


# print("\n\n")
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# combined = zip(scores, grades)
# combined_list = list(combined)
# # print("combined:", combined)       # <zip object at 0x1023a9600>
# # print("\ncombined list: ", combined_list)  # [(90, 'A'), (86, 'B'), (75, 'C'), (91, 'A'), (62, 'D'), (99, 'A'), (88, 'B'), (90, 'A')]
# combined_dict = dict(combined_list)
# print(combined_dict)  # {90: 'A', 86: 'B', 75: 'C', 91: 'A', 62: 'D', 99: 'A', 88: 'B'}



# print("\n\n")
items = ['a', 'b', 'c']

index = 0
for el in items:
    print(el, index)
    index += 1


# for index, element in list(enumerate(items)):
#     print(index, element)
