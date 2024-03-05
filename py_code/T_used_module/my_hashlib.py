import hashlib, random

# md5 = hashlib.md5() #将文本字符编码成utf-8格式，再用md5算法， 后output为十六进制摘要
# md5.update('zhanjie want 2 tao!'.encode('utf-8'))
# md5.update('zhanjie doesnt want 2 tao!'.encode('utf-8'))
# print(md5.hexdigest()) #128bit = 16Bytes, output为32位的16进制字符

# sha1 = hashlib.sha1()#将文本字符串用sha1算法编码成utf-8格式， 后output为十六进制摘要
# sha1.update('zhanjie want 2 tao!'.encode('utf-8'))
# sha1.update('zhanjie doesnt want 2 tao!'.encode('utf-8'))
# print(sha1.hexdigest()) #160bit = 20Bytes, output为40位的16进制字符

# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }

# def login(user, password):
#     password_md5 = calc_md5(password)
#     stored_password_md5 = db.get(user)
#     return stored_password_md5 == password_md5



# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

# def calc_md5(password):
#     return get_md5(password + 'the salt')

def get_md5(user, pws):
    return hashlib.md5((user.username + pws + user.salt).encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(self, password)

db = { # 字典 db 调用 user类 将名字与密码更新（已加密—MD5+salt）
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(user, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')