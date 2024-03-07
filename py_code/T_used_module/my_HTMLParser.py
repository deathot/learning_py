from html.parser import HTMLParser
from urllib import request
from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
    
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print('<!--', data, '-->')
        
#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)
    
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

with request.urlopen('https://www.python.org/events/python-events/') as f:
    html = f.read().decode('utf-8')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.flag = ''
        self.info = []

    def handle_starttag(self, tag, attrs):
        if not attrs: return        
        atr = attrs[0][1]
        if atr == 'event-title':
            self.flag = 'title'        
        elif tag == 'time':
            if atr == 'say-no-more':
                self.flag = 'year'            
            elif attrs[0][0] == 'datetime':
                self.flag = 'date'        
        elif atr == 'event-location':
            self.flag = 'location' 
   
    def handle_endtag(self, tag):
        self.flag = ''    

    def handle_data(self, data):
        if self.flag == 'title':
            self.info.append(f'会议名称:{data}')
        elif self.flag == 'year':
            self.info.append(f'会议年份:{data.strip()}')
        elif self.flag == 'date':
            self.info.append(f'会议时间:{data}')
        elif self.flag == 'location':
            self.info.append(f'会议地点:{data} \n')

parser = MyHTMLParser()
parser.feed(html)
for n in parser.info:
    print(n)