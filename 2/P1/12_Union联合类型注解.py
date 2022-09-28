# 引用 Union 包
from typing import Union

list1: list[Union[int, str]] = [1, 2, "aa", "bb"]


def func(data: Union[int, str]) -> Union[int, str]:
    pass


func()