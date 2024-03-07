#URL-（Uniform Resource Locator）统一资源定位符
# XML-（Extensible Markup Language）可扩展标记语言
# HTML-（HyperText Markup Language）超文本标记语言
from xml.parsers.expat import ParserCreate

# class DefaultSaxHandlerd(object):
    
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

#     def end_element(self, name):
#         print('sax: end_element: %s' % name)

#     def char_data(self, text):
#         print('sax: char_data: %s' % text)
    
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handler = DefaultSaxHandlerd()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

# L = []
# L.append(r'<?xml version = "1.0""?>')
# L.append(r'<root>')
# L.append(encode('some & data', 'utf-8'))
# L.append(r'</root>')
# return ''.join(L)

from xml.parsers.expat import ParserCreate

from urllib import request,parse

import json

#jingle adcode:140926 citycode:0350

#高德地图申请的查询天气key:

weather_Key = '5e665640b3b31ce4846b9b4a12851999'


#将城市名称转换为URL编码

address=parse.quote('山西省')

adcode = 140926

#通过已经获得的城市adcode获得该城市的天气情况

with request.urlopen('https://restapi.amap.com/v3/weather/weatherInfo?key=%s&city=%s&output=xml'%(weather_Key,adcode)) as f:

    xmlre=f.read().decode('utf-8')

#建立SAX

class DefaultSaxHander(object):

    def start_element(self,name,attrs):

        print('sax:start_element:%s,attrs:' % name)

    def end_element(self,name):

        print('sax:end_element:%s' % name)

    def char_element(self,text):

        print('sax:char_element:%s' % text)

hander=DefaultSaxHander()

parser=ParserCreate()

parser.StartElementHandler=hander.start_element

parser.EndElementHandler=hander.end_element

parser.CharacterDataHandler=hander.char_element

#解析所获得的xml格式的天气数据：

parser.Parse(xmlre)
