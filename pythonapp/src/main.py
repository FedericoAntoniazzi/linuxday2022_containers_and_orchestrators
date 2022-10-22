from datetime import datetime
from time import sleep

# This is a bug, fix me
now = datetime.now()

for i in range(100):
    print(now.strftime("%H:%M:%S"))
    sleep(1)
