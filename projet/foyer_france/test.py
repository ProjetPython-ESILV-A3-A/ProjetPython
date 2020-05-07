import datetime
import time

teme = datetime.datetime.utcnow().timestamp()
print(teme)
print(time.time())

date = datetime.datetime.fromtimestamp(teme)

print(date)