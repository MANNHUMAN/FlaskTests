import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_thing(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done sleeping.'

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_thing, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

threads=[]

#for _ in range(10):
#    t=threading.Thread(target=do_thing, args=[1.5])
#    t.start()
#    threads.append(t)
#
#for thread in threads:
#    thread.join()

#t1=threading.Thread(target=do_thing)
#t2=threading.Thread(target=do_thing)
#
#t1.start()
#t2.start()
#
#t1.join()
#t2.join()

print('Finished')
input('...')