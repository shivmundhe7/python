import os
import time 

REPEAT_INTERVAL = 3600 

while True:
  command = "osascript -e \'say \"Hey Shiv drink water\"\'; osascript -e \'display alert \"Hey Shiv, Drink water\"\'"
  os.system(command)
  time.sleep(REPEAT_INTERVAL)