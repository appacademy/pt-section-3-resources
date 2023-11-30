# CONSTANT_HELLO = "hello"
# print(CONSTANT_HELLO)
# CONSTANT_HELLO = 1

# print(CONSTANT_HELLO)

# num_a = num_b = num_c = 0

# print(num_a)
# print(num_b)
# print(num_c)

# num_a = 5

# num_b = 3

# print(num_a // num_b)

# num = ""

# print(num)

# print(isinstance(num, str))

# num = 1.1

# num = float(1.1)

# print(isinstance(num, float))

# different ways to make strings
# string = 'hello world'
# string = ""
# string = """"""
# string = str()
# string = f""

# strings are immutable, this prints a type error
# string[1] = 'z'

# print(string)
# print(isinstance(string, str))

# list, same as array in JS
# nums = [1,2,3,4,5]
# nums = list([1,2,3,4,5])
# strings = list(['hello', 'sfdasf'])
# print(nums)
# print(strings)
# print(nums[1])
# nums[1] = 22
# print(nums[1])

# dictionary, same as object in JS

# state_capitals = {"California": "Sacramento", "Arizona": "Phoenix", "Wisconsin": "Madison"}
# state_capitals = dict({"California": "Sacramento", "Arizona": "Phoenix", "Wisconsin": "Madison"})


# can't use dot notation for dictionaries to access keys
# print(state_capitals.California)

# California = "California"


# print(state_capitals[California])
# print(state_capitals["Arizona"])
# print(state_capitals.get("Wisconsin"))

# sets
# even_numbers = {2,4,6,8,10}
# print(even_numbers)
# print(isinstance(even_numbers, set))
# print(isinstance(state_capitals, set))
# even_numbers.add(12)
# print(even_numbers)
# even_numbers.add(10)
# print(even_numbers)
# even_numbers.add("12")
# print(even_numbers)

# nums = {1, 1, 1}
# print(nums)


# tuples
# odd_numbers = (1,3,5,7,9,11,13)
# odd_numbers = tuple((1,3,5,7,9,11,13))
# print(odd_numbers)
# print(odd_numbers[1])
# odd_numbers[1] = 5


# def print_hello():
#     print("Hello")

# print(print_hello())

# my_int = 4
# my_float = 4.0

# print(my_int == my_float)

# list_1 = [1,2,3]
# list_2 = [1,2,3]

# print(list_1 == list_2)

# a = "1"
# b = 1
# print(id(a))
# print(a is b)
# print(id(list_1))
# print(id(list_2))
# print(list_1 is list_2)

# empty_list = None

# if empty_list is not None:
#     print("not none")
# else:
#      print("its none")

# day_time = True

# if day_time == True:
#     print('its true')

# if day_time is True:
#     print('its true')

# a = []
# b = a
# print(a is b)

# print(1 is 1)

count = 0
y = 'y'
e = 'e'
a = 'a'
h = 'h'
# while condition:
# while (index < 10):
#     pass
while count < 10:
    a += 'a'
    count += 1
# print(y + e + a + h)

nums = [1,3,5,7,9,12,14]

index = 0
# print(len(nums))
# while index < len(nums):
#     print(index)
#     if nums[index] % 2 == 0:
#         break
#     else:
#         nums[index] += 1
#     index += 1

# print(nums)

# for element in iterable:
# for num in nums:
#     print(num)

# print(15 in nums)

num = 0
# print(4/num)

try:
    print(4/num)
except ZeroDivisionError:
    print("Can't divide by 0")
else:
    print("Successfully divided!")
finally:
    print("Finished doing stuff")

class Test:
    pass
