import time
from functools import lru_cache

# lru is least recently used cache
# suppose a func takes 3 sec to execute now for some reason
# we want to execute the same func again it will take again 
# 3 sec to execute for same args
# with lru cache what we do is store value that function returns
# so next time the same function is called it can return value
# instantly

# maxsize =3 means it will store latest 3 calls

@lru_cache(maxsize=3)
def work(n):
    time.sleep(3)
    # print("done")
    return n    

print("Running")
work(3)
print("Done...calling again")
work(3)
print("Done")
