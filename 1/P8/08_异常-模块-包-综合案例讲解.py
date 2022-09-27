
import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("str1"))
print(my_utils.str_util.substr("str1", 0, 2))

file_util.print_file_info("E:/Code/python-note/1/P7/test.txt")
file_util.append_to_file("E:/Code/python-note/1/P8/write.txt", "999")

file_util.append_to_file()
