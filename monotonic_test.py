import time

while True:
    start_time = time.monotonic()
    # 1초 대기
    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time
        if elapsed_time >= 1:
            break
    
    print("1초마다 반복합니다.")




    