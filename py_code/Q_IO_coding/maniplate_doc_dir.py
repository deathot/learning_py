# import os
# os.name
# os.unmae()
# os.environ
# os.environ.get('PATH')
# os.enrion.get('X', 'default')
# os.path.abspath('.')
# os.path.join('E:\\', 'testdir')
# os.mkdir('E:\\testdir')
# os.rmdir('E:\\testdir')

import os
import time
# 获取当前工作目录
cwd = os.getcwd()
# 获取当前目录下的所有文件和文件夹
items = os.listdir(cwd)
# 遍历每个项目
for item in items:
    # 获取项目的绝对路径
    path = os.path.join(cwd, item)
    # 获取项目的状态信息
    stat = os.stat(path)
    # 获取项目的大小，单位为字节
    size = stat.st_size
    # 获取项目的最后修改时间，单位为秒
    mtime = stat.st_mtime
    # 格式化时间为年-月-日 时:分:秒
    mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
    # 判断项目是文件还是文件夹
    if os.path.isfile(path):
        # 如果是文件，输出文件名，大小和修改时间
        print(f'{item}\t{size}\t{mtime}')
    elif os.path.isdir(path):
        # 如果是文件夹，输出文件夹名，<DIR>标识和修改时间
        print(f'{item}\t<DIR>\t{mtime}')

# 定义一个函数，接受一个目录和一个字符串作为参数
def find_files(dir, string):
    # 获取目录下的所有文件和文件夹
    items = os.listdir(dir)
    # 遍历每个项目
    for item in items:
        # 获取项目的绝对路径
        path = os.path.join(dir, item)
        # 判断项目是文件还是文件夹
        if os.path.isfile(path):
            # 如果是文件，判断文件名是否包含指定字符串
            if string in item:
                # 如果包含，打印文件的相对路径
                print(os.path.relpath(path))
        elif os.path.isdir(path):
            # 如果是文件夹，递归调用函数，继续搜索子目录
            find_files(path, string)

# 获取当前工作目录
cwd = os.getcwd()
# 输入要查找的字符串
string = input('请输入要查找的字符串：')
# 调用函数，从当前目录开始搜索
find_files(cwd, string)
