def list_while_func():
    """
    while 遍历
    :return: None
    """
    my_list = [1, 2, 3]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1


def list_for_func():
    """
    for 遍历
    :return: None
    """
    my_list = [1, 2, 3, 4, 5]
    # 无需len
    for element in my_list:
        print(element)


list_while_func()
list_for_func()