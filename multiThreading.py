import threading
import time

# indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    
time1 = time.perf_counter()   # used to calculate performance 
# # 1. code without threading which causes to run the function one by one
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()    # calculating time taken by code without Threads
# print(time2 - time1)

# 2. same code using Threads causes fn to run parallely 
t1 = threading.Thread(target= func, args=[4])
t2 = threading.Thread(target= func, args=[2])
t3 = threading.Thread(target= func, args=[1])
t1.start()   
t2.start()     # this will start running the t2 thread without letting t1 stop => time taken by this code without join()= 0.0016
t3.start()

# t1.join()
# t2.join()     # this will let t1 stop before t2 starts running => time taken = 4.003
# t3.join()

# calculating time taken by Threads code
time3 = time.perf_counter()
print(time3 - time1)

#-------Another way---------#

## using ThreadPoolExecutor with map() => helps in scheduling tasks in bulk
# from concurrent.futures import ThreadPoolExecutor
# import time

# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)
#     return seconds
    
# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         l = [3,5,1,2]
#         results = executor.map(func, l)
#         for result in results:
#             print(result)

# poolingDemo()