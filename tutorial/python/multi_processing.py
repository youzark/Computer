import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"sleep {seconds} second")
    time.sleep(seconds)
    return f"sleep done {seconds}"

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [9,8,7,6,5,4,3,2,1]
    results = executor.map(do_something,secs)
    for result in results:
        print(result)
#   results = [executor.submit(do_something,sec) for sec in secs]
#   for f in concurrent.futures.as_completed(results):
#       print(f.result())



end = time.perf_counter()
during = end - start

print(f"finished in {round(during,3)} seconds")
