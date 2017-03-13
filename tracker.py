import os
import time
from datetime import datetime, timedelta

while True:
    os.system("sudo python3 /services/python/flights/getGF.py 1")
    os.system("sudo python3 /services/python/flights/analyseGF.py 1")

    now = datetime.now()
    next = now + timedelta(minutes=30)
    next -= timedelta(minutes=next.minute % 30,
                      seconds=next.second,
                      microseconds=next.microsecond)
    pause = (next - now).total_seconds()

    time.sleep(pause)
