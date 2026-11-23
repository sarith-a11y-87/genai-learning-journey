# Strings- working with textual data
# m = 'Bobby\'s birthday is on 12/12/2012'
# m = "Bobby's born in 12/12/2012"
# name = "Bobby"
# date = "12/12/2012"
# print(m)
# print(len(m))
# print(m[0])
# print(m[0:5])
# print(m[5:])
# print(m.lower())
# print(m.count('b'))
# print(m.lower().count('b'))
# print(m.replace('12/12/2012', 'hello'))
# print('{}, your birthday is on {}'.format(name, date))
# print(f'{name}, your birthday is on {date}')

# Integer and float numbers
# num = 3.04
# print(num)
# print(3/2)
# print(3//2)  # floor division
# print(3*2) 
# print(3**2)  # exponentiation
# print(3%2)  # modulo
# x = 2
# x += 1
# x *= 2
# print(x)
# print(round(3.14159))


# Lists. Tuples and Sets
# courses = ["Python", "Java", "C++"]
# courses.append("C#")
# courses.insert(0, "JavaScript")
# courses.remove("C++")
# courses.insert(2, ["C", "GO"])
# print(courses)
# print(courses[2])
# print(courses[-1])
# courses.reverse()
# print(courses)
# print(courses.index("Java"))
# print('Java' in courses)

# for item in courses:
#     print(item)

# for index, item in enumerate(courses, start=1):
#     print(index, item)

# cources = ["Python", "Java", "C++"]
# courses_str = " -- ".join(cources)
# print(courses_str)

# num = [1, 2, 3, 4, 5]
# num.sort(reverse=True)
# print(num)

# Mutable vs Immutable (Tuples)
# Mutable
# list_1 = [1, 2, 3]
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1.append(4)
# print(list_1)
# print(list_2)

# # Immutable
# tuple_1 = ('History', 'Maths', 'English', 'Science')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Geography'

# print(tuple_1)
# print(tuple_2)

## Sets
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6, 7, 8}

# print(set_1)
# print(3 in set_1)
# print(set_1.intersection(set_2))
# print(set_1.union(set_2))


#Empty list
# empty_list = []
# empty_list = list()

#Empty tuple
# empty_tuple = ()
# empty_tuple = tuple()

#Empty set
# empty_set = {}  # This is a dict, not a set
# empty_set = set()

# Dictionaries
student = {
    "name": "Bobby",
    "age": 20,
    "courses": ["Python", "Java", "C++"]
}
student['age'] = 21
print(student)
print(student['age'])
print(student.get('hello', 'not found'))

# del student['age']
# age = student.pop('name')
# print(student)
# print(age)
# print(student.keys())
# print(student.values())
# print(student.items())

for key, value in student.items():
    print(key, value)