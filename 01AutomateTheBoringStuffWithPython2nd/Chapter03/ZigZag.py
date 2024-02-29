import time
import sys

time.sleep(0.1)
increment = 0
increacing = True
try:
    while True:
        print(" " * increment, end="")
        print("*******")
        time.sleep(0.1)
        if increment == 20:
            increacing = False
        elif increment == 0:
            increacing = True
        if increacing:
            increment = increment + 1
        else:
            increment = increment - 1
except KeyboardInterrupt:
    sys.exit()
