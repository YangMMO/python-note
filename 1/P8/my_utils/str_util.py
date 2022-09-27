"""
字符串模块
"""


def str_reverse(s):
    """
    字符串反转
    :param s: 字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    字符串切片
    :param s: 字符串
    :param x: 起始下标
    :param y: 结束下标
    :return: 切片后的字符串
    """
    return s[x: y]


if __name__ == '__main__':
    str1 = "mmoofun"
    str1 = str_reverse(str1)
    print(str1)
    print("______________________")

    str1 = "mmoofun"
    str1 = substr(str1, 0, 3)
    print(str1)
