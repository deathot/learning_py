# import sys

# print(sys.argv)
# soucre = sys.argv[1]
# target = sys.argv[2]

import argparse

def main():
    parser = argparse.ArgumentParser(
        prog = 'my_argparse',
        description = 'back up MySQL database.',
        epilog = 'Copyright(r), 2024'
    )
    parser.add_argument('outfile')#positional parameters
    parser.add_argument('--host', default = 'localhost')#ip
    parser.add_argument('--port', default = '3306', type = int)
    parser.add_argument('-u', '--user', required = True)
    parser.add_argument('-p', '--password', required = True)
    parser.add_argument('--database', required = True)
    parser.add_argument('-gz', '--gzcompress', action = 'store_true', required = False, help = 'Compress backup filzes by gz.')
    
    #解析参数
    args = parser.parse_args()
    
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()

# (deathot312) C:\AppsC\Vscode\learning_py-main\py_code\T_used_module>python my_argparse.py -u deathot -p hello --database
#  testdb backup.sql
# parsed args:
# outfile = backup.sql
# host = localhost
# port = 3306
# user = deathot
# password = hello
# database = testdb
# gzcompress = False