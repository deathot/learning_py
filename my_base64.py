import base64
# base64.b64encode(b'binary\x00string')
# base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
# base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# base64.urlsafe_b64decode(b'abcd--__')

#standar base64
# 'abcd' -> 'YWJjZA=='
#自动去掉=:
# 'abcd' -> 'YWJjZA'

#test

# def safe_base64_decode(s):
#     if len(s) % 4 == 0:  
#         return base64.urlsafe_b64decode(s)
#     else:
#         s += '='
#         return safe_base64_decode(s)

def safe_base64_decode(s):
    padding = (4- len(s) % 4)
    if padding and padding != 4:
        s += '=' * padding
    return base64.urlsafe_b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')