# Conditions and Booleans - If, Else, Elif
# x = 10
# if x == 10:
#     print("This will be printed")
# else:
#     print("This will not be printed")

# user = "Admin"
# logged_in = True
# if user == "Admin" or logged_in:
#     print("Admin page")
# else:
#     print("Not authorized")

# if not logged_in:
#     print("Please log in")
# else:
#     print("Welcome back")

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)
# a = b
# print(id(a))
# print(id(b))
# print(a is b)


# condition = []
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")


# Loops and Iterations - For, While
# For loop
# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print("Found!")
#         continue
#     print(num)

# for num in nums:
#     for letter in "abc":
#         print(num, letter)

# for i in range(1, 11):
#     print(i)

#While loop
# i = 1
# while i <= 10:
#     if i == 5:
#         print("Found!")
#         i += 1
#         continue
#     print(i)
#     i += 1


# Functions
def hello_func(greeting, name):
    return f"{greeting}, {name}"

print(hello_func("Hello", "John"))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
student_info("Math", "Art", name="John", age=22)
