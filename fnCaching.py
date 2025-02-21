from functools import lru_cache
import time

@lru_cache()
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(4))
print("Done for 4")
print(fx(26))
print("Done for 26")
# for the above value output will be displayed after 5 sec
print(fx(20))
print("Done for 20")      # for this and 4 below, lru_cache take the result from cache as it is already computed previously
# therefore, output will be displayed instantly & not after 5 sec
print(fx(4))
print("Done for 4")
print(fx(47))
print("Done for 47")