import os
import time

while True:
    print("Start: %s" % time.ctime())
    os.system("sudo python3 /services/python/flights/getGF.py 1")
    os.system("sudo python3 /services/python/flights/analyseGF.py 1")
    print("End: %s" % time.ctime())
    time.sleep(1800)
