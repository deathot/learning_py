import hmac, random
# message = b'Hello, world!' # 字节类型字符串 ASCII
# key = b'secret'
# h = hmac.new(key, message, digestmod='MD5')
# h.update(b'012')
# # 如果消息很长，可以多次调用h.update(msg)
# print(h.hexdigest())
# # 'fa4ee7d173f2d97ee79022d1a7355bcf'

#test

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])#character-字符
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')