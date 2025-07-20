import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(6)    #Stimulate some work
    print(f"Thread {num}: Ending")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()   #Immediately start the execution of the another thread

for thread in threads:
    thread.join()    # Wait for alll threads to finish

print("All threads are finished.")