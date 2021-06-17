import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    print('Done Sleeping')

thread_list = []
for _ in range(10):
    t = threading.Thread(target = do_something,args=[1.5])
    thread_list.append(t)
    t.start()

for thread in thread_list:
    thread.join()


finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')
