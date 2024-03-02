import re

# reEmail = re.compile(r'^[\w\.\s<>]+@[\w\.\s<>]+$')
# print(reEmail.pattern)
# def is_valid_email(addr):
#     return reEmail.match(addr)


# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

reEmail1 = re.compile(r'^([\w\.\s<>]+)@[\w\.\s<>]+$')
reEmail2 = re.compile(r'<?([\w\.\s]+)>?')
def name_of_email(addr):
    match = reEmail1.match(addr)
    if match:
        res = reEmail2.match(match.group(1)).group(1)
        return res
    return None

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')