import time
from datetime import datetime


f = open("time_test.txt")


time_string = str(f.readline())


fmt = "%Y-%m-%dT%H:%M:%S"


parsing_string = time.strptime(time_string, fmt)


print(time.strftime("It's %A, %B %d, %Y, local time %I:%M:%S", parsing_string))



