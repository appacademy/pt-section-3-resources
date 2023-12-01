# def greeter(name):
#     print(f"Hello, {name}")

# def greeter(name):
#     return f"Hello, {name}"

# print(greeter("Tiffany"))

# y = 5
# only functions and classes create local scopes
# def print_num():
#     x = 5
    # print(x)
    # print(y)

# print_num()

# print(x)
# if True:
    # x = 5
# print(x)
# these do not create a local scope
# while:
# for:
# if:
# else:
# try:

# def num_halfer(num):
#     """
#     Takes a num and divides it by 2 then returns the result
#     anything
#     """
#     return num / 2

# dunder __something__
# print(num_halfer.__doc__)
# help(num_halfer)

# print(num_halfer(20))

# javascript ...args == python *args
# have to follow this order for passing parameters/arguments: positional, *args, **kwargs
# def math_operations(multiplier, divider, *nums, power_num = 1, integer_divisor = 1):
#     count = 0
#     for num in nums:
#         # count = count + num
#         count += num
#     count *= multiplier
#     count /= divider
#     count **= power_num
#     count //= integer_divisor
#     return int(count)

# print(math_operations(4,3,5,3,1,integer_divisor = 100, power_num=5,))

# is_even = lambda num: num % 2 == 0

# print(is_even(5))

nums = [1,2,3]
nums = list([1,2,3])

print(nums)

print(nums[0])
print(nums[0:len(nums)])
