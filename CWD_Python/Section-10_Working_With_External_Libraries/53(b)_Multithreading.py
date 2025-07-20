import threading
import time

print_lock = threading.Lock()

def worker(num):
    with print_lock:
        print(f"Thread {num}: Starting")
    time.sleep(2)
    with print_lock:
        print(f"Thread {num}: Ending")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads are finished.")