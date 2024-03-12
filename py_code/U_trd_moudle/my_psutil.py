# psutil == process and system utilities

import psutil

psutil.cpu_count()
psutil.cpu_count(logical = False)
psutil.cpu_times()

for x in range(10):
    print(psutil.cpu_percent(interval = 1, percpu = True))

psutil.virtual_memory()
psutil.swap_memory()

psutil.disk_partitions()
psutil.disk_usage('/')
psutil.disk_io_counters()

psutil.net_io_counters() #网络读写字节/包的个数
psutil.net_if_addrs() #网络接口信息
psutil.net_if_stats() #网络接口状态
psutil.net_connections() #当前网络连接信息
psutil.pids() #所有进程ID

p = psutil.Process(3736)
p.name()
p.exe()
p.cwd()
p.cmdline()
p.ppid()
p.parent()
p.children()
p.status()
p.username()
p.create_time()
p.terminal()

psutil.test()