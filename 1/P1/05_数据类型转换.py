# <class 'str'> 11
numToStr = str(11)
print(type(numToStr), numToStr)

# <class 'str'> 12.6
floatToStr = str(12.6)
print(type(floatToStr), floatToStr)

# <class 'int'> 15 不四舍五入
floatToInt = int(15.6)
print(type(floatToInt), floatToInt)

# <class 'float'> 12.0
strToFloat = float('12')
print(type(strToFloat), strToFloat)

# ValueError: invalid literal for int() with base 10: 'ddd'
# strToInt = int('ddd')
# print(type(strToInt), strToInt)
