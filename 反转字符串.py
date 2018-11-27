from functools import reduce

str = 'chengchao001'
# 1.使用切片进行反转
print("method1 %s" % str[::-1])

# 2. 转换成列表
l = list(str)
l.reverse()
l1 = ''.join(l)
print("method2 %s" % l1)

# 3.使用reduce函树
result = reduce(lambda x, y: y + x, str)
print("method3 %s" % result)


# 4. 使用递归函数
def func(s):
    if len(s) < 1:
        return s
    return func(s[1::])+s[0]


print("method4 %s" % func(str))


# 5. 使用栈
def func1(s):
    l = list(s)
    result = ''
    while len(l) > 0:
        result += l.pop()
    return result


print("method5 %s" % func1(str))
