# test = ["item", [], []]
# print(any(test)) # True
# print(all(test)) # False

# def mapper_func(el):
#     return el * 3

# lst = [1, 2, 3]

# mapped_object = map(lambda x: x * 3, lst)
# mapped_object = map(mapper_func, lst)
# # print(list(mapped_object))
# mapped_arr = list(mapped_object)

# def filter_func(el):
#     print("Was I printed?", el)
#     return not (el % 2)


# # filter_object = filter(lambda el: not (el % 2), mapped_arr)
# filter_object = filter(filter_func, mapped_arr)

# print(list(filter_object))


iterable_list = iter([1, 2, 3])
# print(iterable_list)
# print(list(iterable_list))


# # for el in items:
# #     print(el)

# for index in range(len(items)):
#     print(index)
#     print(items[index])


# ENUMERATE

# iterable_obj = iter([1,2,3])

# print(next(iterable_obj))
# # print(list(iterable_obj))
# print(next(iterable_obj))
# print(next(iterable_obj))
# print("HERE IS THE ERROR:")
# print(next(iterable_obj))
# print(list(iterable_list))

# def my_gen():
#     yield "hello"

# print("My Gen obg", my_gen())
# print("My Gen", list(my_gen()))




def my_map_under_the_hood(function, *iterables):

    iterables = [iter(iterator) for iterator in iterables]

    # print("My Map Iterables: ", iterables)

    while True:
        try:
            elements = [next(it) for it in iterables]
            # print("My Map Elements: ", elements)

            yield function(*elements)
        except StopIteration:
            # print("my map error")
            break

def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

iterable_list = list([1])
iterable_list2 = list([2, 4, 6])
iterable_list3 = list([10, 100, 1000])

answer = my_map_under_the_hood(my_func, iterable_list, iterable_list2, iterable_list3)
print("Answer: ", answer)
print("List Answer: ", list(answer))




def mapper_func(el1):
    # print(el1, el2)
    return el1 * 2

lst1 = [2, 2, 2, 120]
mapped_obj = map(mapper_func, lst1)


# lst2 = [2, 4, 6]
# lst3 = [2, 4, 6, 8]
# print("TEST", mapped_obj/)
# print("HERE", list(mapped_obj))













# enumerated_items = enumerate(items)
# print(enumerated_items)
# print(list(enumerated_items))

# for idx, ele in list(enumerated_items):
#     print(idx, ele)


# phones = [
#     {
#         "brand": "Apple",
#         "model": "iPhone 13 Pro",
#         "cost": 929,
#         "color": "alpine green"
#     },
#     {
#         "brand": "Samsung",
#         "model": "Galaxy S22+",
#         "cost": 999,
#         "color": "black"
#     },
#     {
#         "brand": "Google",
#         "model": "Pixel 6",
#         "cost": 599,
#         "color": "kinda coral"
#     },
#     {
#         "brand": "Apple",
#         "model": "iPhone 13 Pro",
#         "cost": 929,
#         "color": "gold"
#     },
#     {
#         "brand": "Google",
#         "model": "Pixel 6",
#         "cost": 599,
#         "color": "stormy black"
#     }
# ]

# # Write your code here.


# def get_unique_models(phone_list):
#     unique_phones = []
#     seen_models = []
#     for phone in phone_list:
#         if phone['model'] not in seen_models:
#             seen_models.append(phone['model'])
#             unique_phones.append(phone)
#     return unique_phones

# def map_to_names(phone_list):
#     map_obj = map(lambda el: el["model"], phone_list)
#     return list(map_obj)

# unique_models = list(get_unique_models(phones))
# print(unique_models)                # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
# print(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6
