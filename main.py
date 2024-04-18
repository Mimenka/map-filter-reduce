from functools import reduce
# 1.
my_list = [1,2,3,4,5]
new_list = reduce(lambda x, y: x + y, my_list )
print(new_list)

# 2.
numbers = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x**2, numbers))
print(new_list)

# 3.
numbers = [4, 7, 2, 9, 1]
new_list = reduce(lambda x, y: x if x < y else y, numbers)
print(new_list)

# 4.
strings = ['1', '2', '3', '4', '5']
new_list = list(map(lambda x: int(x), strings))
print(new_list)

# 5.
strings = ['apple', 'banana', 'cherry', 'grape', 'watermelon']
substring = 'an'
print(list(filter(lambda x: x if substring in x else None, strings)))

# 6.
numbers = [15, 20, 25, 30, 35, 40]
divisor = 5
print(list(filter(lambda x: x % divisor == 0, numbers)))

# 7.
numbers = 12345
print(sum(map(lambda x: int(x), str(numbers))))
