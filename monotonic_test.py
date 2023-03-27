import time

start_time = time.monotonic()

while True:
    current_time = time.monotonic()
    elapsed_time = current_time - start_time
    if elapsed_time >= 1:
        break