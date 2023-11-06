# # TUPLES

# tup = ('red', 'blue')
# # # tup[1] = "green"
# # # print(tup)

# tup += ('green', "orange")

# print(tup)


# tup_2 = "Neo", "Trinity", "Morpheus"

# tup_2 = ("Neo", "Trinity", "Morpheus")
# tup_2[1] = "will"
# print(tup_2[1])

# # tup_3 = 1,
# # tup_4 = 2,
# # tup_5 = 3,



# question = [("name", "test"), ("hello", "world")]

# print(question)

# # EMPTY TUPLES
# empty_tuple = ()
# empty_tuple2 = tuple()

# my_dictionary = {}

# # SINGLETON TUPLE
# tup_6 = (1,)
# tup_7 = 2,


# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)


# ran_sum, ran_avg = sum_and_average([1, 2, 3, 4, 5])

# print(ran_avg, ran_sum)



# RANGES
# values = range(start,stop,step)


# vals = range(1,10,2)
# print("here", vals)

# for i in range(5, 0, -1):
#     print(i)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# for i in range(1, 6)/10:
    # print(i)

# vals = range(10)

# # print(list(numbers_range))

# print(tuple(vals))



# lunch = ["wings", "pizza", "turkey", "salmon"]

# for index in range(len(lunch)):
#     print(index, lunch[index])

# more_vals = range(50, 0, -10)
# print(list(more_vals))


# Problem 3 - Factorial
# Write your function, here.
# def factorial(num):
#     total = 1
#     for val in range(1, num + 1):
#         total *= val
#     return total

# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320  # [1, 2, 3, 4, 5, 6, 7, 8]
# print(factorial(12))    #> 479001600

# def recur_fact(num):
#     if num == 1:
#         return num

#     return num * recur_fact(num -1)


# print(recur_fact(1))     #> 1
# print(recur_fact(8))     #> 40320  # [1, 2, 3, 4, 5, 6, 7, 8]
# print(recur_fact(12))    #> 479001600


# COMPREHENSTIONS
# my_list = [1, "2", True, "butter", None]
# my_list_copy = [item for item in my_list]
# print(my_list_copy)
# my_list_copy2 = [*my_list]
# print(my_list_copy)




# nums = [-11, -5, 11, 10, 14]

# my_list_comp = [num * 2 for num in nums]

# print(my_list_comp)

# # mapped_comp = (num for num in nums)
# # print(tuple(mapped_comp))

# # new_list = []
# for num in nums:
#     new_list.append(num * 2)


# print(new_list)


# filtered_comp = [element for element in nums if element > 0]


# print(filtered_comp)



# mapped_and_filtered_comp = [num * 2 for num in nums if num > 0]
# print(mapped_and_filtered_comp)

# names = ['bob', 'jim', 'andrew', 'jane', 'kate']
# cap_comp = [ name.title() for name in names ]
# print(cap_comp)

# users = [user.to_dict() for user in User.query.all()]

# new_list = [return_val for x in iterable if conditional=true]

# users = [
#   {'first_name': 'John', 'last_name': 'Doe', 'membership': 'premium'},
#   {'first_name': None, 'last_name': 'Doe', 'membership': 'premium'},
#   {'first_name': 'John', 'last_name': None, 'membership': 'premium'},
#   {'first_name': 'Jane', 'last_name': 'Smith', 'membership': 'free'},
#   {'first_name': 'Sarah', 'last_name': 'Conner', 'membership': 'free'},
#   {'first_name': 'John', 'last_name': 'Conner', 'membership': None}]
# # #                   (return_val             ) (iteration      ) (filter conditional    )
# incomplete_users = ((users.index(user), user) for user in users if None in user.values())
# # #                (return_val                                                   ) (iteration      ) (filter conditional              )
# premium_users = [{'first_name':user['first_name'],'last_name':user['last_name']} for user in users if user['membership'] == 'premium']

# print('Incomplete: ', incomplete_users)
# print('\nPremium: ', premium_users)

# vowels = 'aeiouAEIOU'
# sentence = 'This is a comprehension?'

# sent_vowels = [char for char in sentence if char in vowels]
# print('\nVOWELS:', sent_vowels)
# #        (return value             ) (iteration       ) (filter conditional)
# evens = ['EVEN' if i%2==0 else 'ODD' for i in range(10)]
# print('\nFRONT IF:', evens)

# Write your function, here.

# def helper(x):
#   print(x)
#   return x[1]



# def index_sort(tup_list):
#   n = 1
#   tup_list.sort(key = helper)
#   return tup_list



# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]







# def my_add(x, y):
#     return x + y

# let my_add = (x, y) => x + y;



"""

let arr = [1,2,3]

console.log(myMappedArr)

# """
# my_list = [1,2,3]

# # let myMappedArr = arr.map(el => el * 2)

# def my_map(x):
#     return x * 2

# my_mapped_arr = map(my_map, my_list)

# print("HERE", my_mapped_arr)
# print("INDEX", my_mapped_arr[0])
# # print(list(my_mapped_arr))

# for i in list(map(lambda el: el * 2, my_list)):
#     print(i)





# let add = (x,y) => x + y


# filter()







# matrix = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 2],
# ]
# for i in matrix:
#     print("NEW PRINT", i)
#     for j in i:
#         print(j)




# flat = [num
#         for row in matrix
#         for num in row]
# print(flat)





# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

# prices = [i
#           if i > 0
#           else 0
#           for i in original_prices]
# print(prices)



def r_sum(lst):
    #base case
    if len(lst) < 1:
        return 0

    #recursive step
    #recursive case
    return lst[0] + r_sum(lst[1:])


print(r_sum([1, 2, 3])) # prints 6

print("hello")
