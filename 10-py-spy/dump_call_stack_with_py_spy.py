import queue
import threading
import time

# Simple pool with max size 1
pool = queue.Queue(maxsize=1)


def worker(name):
    print(f"{name}: waiting for a connection from the pool...")
    conn = pool.get()  # <-- this thread will block if the pool is empty
    print(f"{name}: got connection {conn}")
    time.sleep(2)
    pool.put(conn)
    print(f"{name}: returned connection {conn}")


def broken_returner():
    # "creates" a connection but never returns it to the pool
    time.sleep(1)
    print("broken_returner: created a connection but does NOT put it back")
    # No pool.put(conn) here to simulate a swallowed connection


# Main
threading.Thread(target=worker, args=("worker-1",)).start()
threading.Thread(target=worker, args=("worker-2",)).start()
threading.Thread(target=broken_returner).start()
