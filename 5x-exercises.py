import time

print("5.1")
print(time.time())


minutes_since_epoch = time.time() / 60.0
print(minutes_since_epoch)

hours_since_epoch = minutes_since_epoch / 60.0
print(hours_since_epoch)

days_since_epoch = hours_since_epoch / 24.0
print(days_since_epoch)


current_seconds = int(time.time() % 60)
current_mintues = int(time.time() / 60 % 60)
current_hour = int(time.time() / 60 / 60 % 24)
print(str(current_hour) + ":" + str(current_mintues) + ":" +
      str(current_seconds))
