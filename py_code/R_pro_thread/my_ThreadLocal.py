import threading

# def process_student(name):
#     std = Student(name)
#     do_task_1(std)
#     do_task_2(std)

# def do_task_1(std):
#     do_subtask_1(std)
#     dp_subtask_2(std)

# def do_task_2(std):
#     do_sub_task_2(std)
#     do_sub_task_2(std)
    
# global_dict = {}

# def std_thread(name):
#     std = Student(name)
#     gloabl_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()

# def do_task_1():
#     std = global_dict[threading.current_thread()]
#     ...

# def do_task_2():
#     std = global_dict[threading.current_thread()]

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    
def process_thread(name):
    local_school.student = name
    process_student()
    
t1 = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob',), naem = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


