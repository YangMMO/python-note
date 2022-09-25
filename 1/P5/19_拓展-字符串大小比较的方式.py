"""
演示字符串大小比较
"""

# abc 比较abd
print(f"abd大于abc，结果: { 'abd' > 'abc '}")
# a比较ab
print(f"ab大于a，结果: { 'ab' > 'a'}")
# a比较A
print(f"a 大于A，结果: {'a' > 'A'}")
# key1比较key2
print(f"key2 > key1，结果:{ 'key2' > 'key1' }")

# abd大于abc，结果: True
# ab大于a，结果: True
# a 大于A，结果: True
# key2 > key1，结果:True


print(f"key1a > key2，结果:{ 'key1a' > 'key2' }")
# key1a > key2，结果:False
# 注意： 只能每一位去对比，长度有差异，只拿可对比的最后一个值去对比
