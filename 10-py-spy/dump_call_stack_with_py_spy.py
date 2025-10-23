import threading
import queue
import time

# Pool with a single connection
pool = queue.Queue(maxsize=1)
pool.put("CONN1")  # initially available connection

def worker(name):
    print(f"{name}: waiting for a connection from the pool...")
    conn = pool.get()  # blocks if pool is empty
    print(f"{name}: got connection {conn}")
    time.sleep(3)  # simulate work
    pool.put(conn)
    print(f"{name}: returned connection {conn}")

def broken_returner():
    conn = pool.get()      # Takes connection but does NOT put it back
    print(f"broken_returner: got {conn}, but does NOT put it back")   # connection is lost, so other threads block

# Start threads
threading.Thread(target=broken_returner).start()
threading.Thread(target=worker, args=("worker-1",)).start()
threading.Thread(target=worker, args=("worker-2",)).start()
