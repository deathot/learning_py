import chardet

chardet.detect(b'Hello, world!')

data = '小丑杰'.encode('gbk')
chardet.detect(data)

data = '小丑结果'.encode('utf-8')
chardet.detect(data)

data = 'Jie Guoは歌を聞いて、性格が通り過ぎます'.encode('euc-jp')
chardet.detect(data)