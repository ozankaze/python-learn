# student_count = 1000
# rating = 4.88
# is_published = True
# course_name = "Halo ka Irine"

# #### String
# Menyatakan karakter/kalimat bisa berupa huruf angka, dll (diapit tanda " atau ')

# course = "Python Programming"
# print(len(course))
# # 18
# print(course[0])
# # P
# print(course[0:3])
# # Pyt
# print(course[0:])
# # Python Programming
# print(course[:3])
# # Pyt
# print(course[:])
# # Python Programming

# #### Escape Sequences
# \n -> Adalah garis baru
# link: https://belajarpython.com/tutorial/string-python

# \" -> Python "Programming
# \' -> Python 'Programming
# \\ -> Python \Programming
# \n -> Python
#       Programming

# course = "Python \nProgramming"
# print(course)

# ####  Formatted Strings
#

# first = "Bae"
# last = "Joo-hyun"
# full = f"{len(first)} {4 + 7}"
# print(full)

# #### String Methods
# link: https://belajarpython.com/tutorial/string-python

# course = "  bae joo-hyun"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("joo"))
# print(course.replace("h", "O"))
# print("joo" in course)
# print("Where" not in course)

# #### Numbers

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3
# x += 3
# print(x)

# #### Type Conversion
# int()
# float()
# bool()
# str()

# x = input("x: = ")
# print(type(x))
# <class 'str'>

# y = int(x) + 5
# print(f"x: {x}, y: {y}")
# x: 5, y: 10

# print(y)
