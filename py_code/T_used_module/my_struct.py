# endian:字节序
#整数n转换成字节：（1Bytes = 8bit）
    # 整数 n 转换成4个Bytes
    

# >>> n = 10240099
# >>> b1 = (n & 0xff000000) >> 24
# >>> b2 = (n & 0xff0000) >> 16
# >>> b3 = (n & 0xff00) >> 8
# >>> b4 = n & 0xff
# >>> bs = bytes([b1, b2, b3, b4])
# >>> bs
# b'\x00\x9c@c'

import struct
# with open("001.bmp", "rb")as file:
#     data = file.read()

# struct.pack('>I', 10240099) # I 相当于声明了是4(Bytes无符号整数) 然后通过声明转换成Bytes类型

# struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80') #4 + 2

# print(data)

# s = b'BM6,"\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x80\x04\x00\x00\x88\x02\x00\x00\x01\x00\x18\x00'
# struct.unpack('<ccIIIIIIHH', s)
#(b'B', b'M', 2239542, 0, 54, 40, 1152, 648, 1, 24)

#test

import base64

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

# print(bmp_data)

def bmp_info(data):
    bmp = struct.unpack('<ccIIIIIIHH', data[:30])
    print(bmp[::])
    color = bmp[-1]
    height = bmp[-3]
    width = bmp[-4]
    return{
        'width' : width,
        'height' : height,
        'color' : color
    }
# # 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
    