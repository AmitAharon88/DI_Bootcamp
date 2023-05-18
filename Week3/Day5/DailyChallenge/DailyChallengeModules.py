import requests
from time import time

def load_time(url) :
    start_time = time()  # number of second since the epoch
    requests.get(url)
    end_time = time()
    time_passed = end_time - start_time
    return time_passed

print(load_time('https://www.coolthings.com/'))
print(load_time('https://www.google.com/'))
print(load_time('https://www.youtube.com/'))
print(load_time('https://www.ynet.co.il/home/0,7340,L-8,00.html'))

