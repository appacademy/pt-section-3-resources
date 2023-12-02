# tuples
# even_nums = (2,4,6,8)
# even_nums = tuple((2,4,6,8))
# even_nums = tuple([2,4,6,8])
# print(even_nums)

# tuples are immutable
# nums = (6,2,1,5,1,6)
# print(nums)
# nums.append(1)

# creating empty or singleton tuples
# even_nums = tuple([2])
# nums = ([2,4,6,8],)
# nums = tuple([])
# print(nums)
# even_nums = (2,)
# print(even_nums)
# print(isinstance(even_nums, tuple))

# adding to a tuple
# even_nums = tuple([2,4,6,8,10])
# even_nums = even_nums + (12,)
# print(even_nums)

# sorting tuples
# unsorted_nums = tuple([5,1,8,2341,6,112,5431,3])
# print(tuple(sorted(unsorted_nums)))
# sorted_nums = tuple(sorted(unsorted_nums))
# print(sorted_nums)

# concat tuples
# even_nums = tuple([2,4,6,8,10])
# even_nums = even_nums + (12,)
# print(even_nums)

# ranges
# range(start = 0, stop, step = 1)
# num_range = range(10)
# print(num_range)
# print(list(num_range))
# nums = [5,1,5,88,23,5,1] # length of 7, last index is 6

# for index in range(0, len(nums), 2):
#     print("index", index)
#     print("data", nums[index])

# reversed range
# for index in range(len(nums) - 1, -1, -1):
#     print("index", index)
#     print("data", nums[index])

# list comprehensions
# expression for element in iterable
nums = [1,5,23,7,3,88,3,1,4,2,5]

nums_adder = [num + 1 for num in nums]
# print(nums)
# print(nums_adder)
# print(isinstance(nums_adder, list))

# list comprehension with if
# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums)

# list comprehension with if/else
# even_nums = [num if num % 2 == 0 else -1 for num in nums]
# print(even_nums)

# list comprehension when no element matches the condition
# even_nums = [num for num in nums if num == -1 ]
# print(even_nums)
