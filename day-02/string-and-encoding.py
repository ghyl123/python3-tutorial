# ASCII 通常一个字节
# GB2312 中国制定的编码
# Unicode 通常两个字节
# UTF-8 可变字节编码 1-6字节
print('包含中文的str')

# 使用ord()函数来获取一个字符的整数表示
print(ord('鹏'))

# chr()函数获取相应编码的字符
print(chr(40527))

# 编码使用encode()函数
# 解码使用decode()函数
print('hello,world'.encode('ascii'))
print('好好学习'.encode('utf-8'))
print(b'hello,world'.decode('ascii')) # hello,world
print(b'\xe5\xa5\xbd\xe5\xa5\xbd\xe5\xad\xa6\xe4\xb9\xa0'.decode('utf-8')) # 好好学习

# len()函数可以计算字符串的长度，或者bytes的字节数
print(len('hello'))
print(len('你好'))
print(len('好好学习'.encode('utf-8')))

# 格式化字符串 %s:表示字符串 %d:表示整数 %x:表示16进制数整数 %f:表示浮点数
print('hello, %s' % 'dreamapple')
print('%d-%d-%d' % (2017, 3, 21))