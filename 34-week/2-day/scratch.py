class MyClass:
    def __init__(self):
        self.attribute = "value"


obj = MyClass()

# Regular attribute access
# print(obj.attribute)

# print(obj.__dict__['attribute'])

# my_dict = {'hello': "world", "2": 2, 1: "hi"}
# print(my_dict['hello'])
#
# my_var = "three"

my_dict = {"one": 1, "two": 2, "three": 3}

#DICT COMPREHENSION


# my_new_dict = {k: v for}
# print(my_new_dict)
# print(my_var in my_dict)

# print(my_dict.get("not_a_key"))

# if my_dict.get("not_a_key") is None:
#     my_dict["not_a_key"] = "COOL!"


# print("keys: ", my_dict.keys())
# print("values: ", my_dict.values())
# print("items: ", my_dict.items())

# print(1 in my_dict.values())

# for key, val in my_dict.items():
#     print(key, val)

# print("before: ", my_dict)
# del my_dict["not_a_key"]
# print("after: ", my_dict)


# Write your code here.
def concatenate_dictionaries(lst):
    return {key: val for d in lst for key, val in d.items()}

    answer_dict = {}
    for d in lst:
        for key, val in d.items():
            answer_dict[key] = val
    return answer_dict





lst = [
    {
        'a': 'this',
        'b': 'is'
    },
    {
        'c': 'the',
        'd': 'merged'
    },
    {
        'd': 'dictionary'
    }
]

# print(concatenate_dictionaries(lst))
"""
Prints:
{
    'a': 'this',
    'b': 'is',
    'c': 'the',
    'd': 'dictionary'
}
"""


def merge_lists(lst1, lst2):
    return dict(zip(lst1, lst2))


lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }
my_dict = {1: "hi", 2: "hello"}


my_set = {1,2,3,4,1,1,2,3,3,3,}
# print(my_set)

lst = [1,5,3,6,5,5,5,3]
# print(list(set(lst)))



# no_dupes = set(lst)
# print(list(no_dupes))

# this_is_a_set = set()
# print(type(this_is_a_set))


# evens = {x for x in range(10) if x % 2 == 0}
# print(evens)


# union of two sets
a = {1, 2, 3}
b = {3, 4, 5}
# print(a | b)       # {1, 2, 3, 4, 5}
# print(a.union(b))  # {1, 2, 3, 4, 5}


a = {1, 2, 3, 5}
b = {3, 4, 5}
# print(a ^ b)       #

# print(b - a)       #






def older_people(some_dict):
    return {k: v for k, v in some_dict.items() if v >= 30}

    return_dict = {}
    for k, v in some_dict.items():
        # print(k, v)
        if v >= 30:
            return_dict[k] = v
    return return_dict

my_dict = {"will": 20, "tom": 30, "susie": 26, "jim": 50}
print(older_people(my_dict))
