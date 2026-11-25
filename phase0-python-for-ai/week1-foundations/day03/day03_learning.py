nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I wantt 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)

# Using map and + Lambda
# my_list = list(map(lambda n: n*n, nums))
# print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)

# Using filter and + Lambda
# my_list = filter(lambda n: n % 2 == 0, nums)
# print(list(my_list))

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# Dictionary Comprehension
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(zip(names, heroes))

# I want a dict{'name': 'hero'} for each name, hero in zip(names, heroes)
# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero
# print(my_dict)


# my_dict = {name: hero for name, hero in zip(names, heroes)}
# print(my_dict)

# Set Comprehension
# nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)


# Generator Comprehension
# I want to yelid 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# my_gen = (n*n for n in nums)
# for i in my_gen:
#     print(i)



# Try/Except Blocks for Error Handling
# try:
#     f = open('testfile.txt')
# except Exception:
#     print("Sorry, file does not exist")

# try:
#     with open('testfile.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#         print("File opened successfully")
# except FileNotFoundError as e:
#     print("Sorry, file does not exist" + str(e))
# except Exception as e:
#     print("Sorry, something went wrong. " + str(e))
# finally:
#     print("Executing finally...")


print('Improted day03_learning')

test = 'Test string'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

