import time, threading, multiprocessing

# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s end.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target = loop, name = 'LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# balance = 0
# lock = threading.Lock()


# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
    
# def run_thread(n):
#     for i in range(5):
#         lock.acquire()
#         try:
#             change_it(n)
#             print('thread %s is running...' % threading.current_thread())
#         finally:
#             lock.release()
    
# t1 = threading.Thread(target = run_thread, args = (5, ))
# t2 = threading.Thread(target = run_thread, args = (8, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


def loop():
    x = 0
    while True:
        x = x ^ 1
    
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target = loop)
    t.strat()