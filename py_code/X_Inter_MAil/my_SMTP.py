from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
# from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib
#LVGDFFOLEHYUKLQV

# msg = MIMEText('Hello, send by python...', 'plain', 'utf-8')

# from_addr = '18920828188@163.com'
# password = 'LVGDFFOLEHYUKLQV'

# to_addr = '2899628422@qq.com'
# smtp_server = 'smtp.163.com'
# port = 25

# server = smtplib.SMTP(smtp_server, port)
# # server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '18920828188@163.com'
password = 'LVGDFFOLEHYUKLQV'
to_addr = '2899628422@qq.com'
smtp_server = 'smtp.163.com'
port = 465

msg = MIMEMultipart('alternative')
msg['from'] = _format_addr('deathot <%s>' % from_addr)
msg['To'] = _format_addr('heathot <%s>' % to_addr)
msg['Subject'] = Header('SMTP...', 'utf-8').encode()

msg.attach(MIMEText('Hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hell4</h1></body></html>', 'html', 'utf-8'))

# with open('/Apro/pic/003.bmp', 'rb') as f:
#     mime = MIMEBase('image', 'bmp', filename = '003.bmp')
#     mime.add_header('Content-Disposition', 'attachment', filename= '003.bmp')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)
#     msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, port)
# server.starttls()
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage