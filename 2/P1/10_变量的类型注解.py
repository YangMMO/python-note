#
import json
import random

var_1: int = 10
var_2: str = "123"
var_3: bool = True


#
class Student:
    pass


stu: Student = Student()


#
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"666": 666}


#
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, int, int] = (1, 2, 3)
my_dict: dict[str, int] = {"666": 666}


# type 注解
var_4 = random.randint(1, 10)           # type: int
var_5 = json.loads('{"name": "aaa"}')   # type: dict[str, str]


def func():
    return 10


var_6 = func()                          # type: int
