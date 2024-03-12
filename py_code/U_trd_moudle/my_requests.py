import requests

# r = requests.get('https://www.bilibili.com/')
# r. status_code
# r.text

# r = requests.get('https://www.bilibili.com/', params = {'q': 'python', 'cat': '1001'})
# r.url
# r.encoding
# r.content

# r = requests.get('https://www.bilibili.com/&format = json')
# r.json()

# r = requests.get('https://www.bilibili.com/', headers = {'pass'})
# r.text

# r = requests.post('https://www.bilibili.com/', data = {'pass'})

url = 'https://www.bilibili.com/'
# params = {'key': 'value'}
# r = requests.post(url, json = params)

# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files = upload_files)

r = requests.get('https://www.bilibili.com/')
r.headers
r.headers['Content-Type']


r.cookies['ts']
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)
r = requests.get(url, timeout=2.5)