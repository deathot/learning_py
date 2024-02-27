# E:
# f = open('test.txt', 'r', encoding = 'utf-8', errors = 'ignore')
# f.read()
# f.close

# try:
#     f = open('test.txt', 'r', encoding = 'utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('test.txt', 'r', encoding = 'utf-8') as f:
#     print(f.read())
# #read(), read(size), readlines()
# for line in f.readlines():
#     print(line.strip())

# f = open('test.txt', 'w')
# f.wirte('Hello, world!')
# f.close()

# with open('test.txt', 'w', encoding = 'utf-8') as f:
#     f.wirte('hello ,world')

#test
fpath = 'test.txt'

with open(fpath, 'r', encoding = 'utf-8', errors = 'ignore') as f:
    s = f.read()
    print(str(s))