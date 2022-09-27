"""
文件模块
"""


def print_file_info(file_name):
    """
    打印文件内容
    :param file_name: 文件路径
    :return: None
    """
    f = None

    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as err:
        print("error: ")
        print(err)
    finally:
        # 假设无法读取文件，则f还是None, 所需需判断是否需要close()
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    将数据插入至文件
    :param file_name: 文件名
    :param data: 数据
    :return: None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("E:/Code/python-note/1/P7/test.txt")
    print("__________")

    print_file_info("E:/Code/python-note/1/P7/error.txt")
    print("__________")

    append_to_file("E:/Code/python-note/1/P8/write.txt", "666")
    print("__________")
