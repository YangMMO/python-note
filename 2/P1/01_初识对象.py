class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None


s1 = Student()
s1.name = "mmo"
s1.gender = "m"
s1.nationality = "aaa"
s1.native_place = "bbb"
s1.age = 21

print(s1.name)

# <class '__main__.Student'>
print(type(s1))
