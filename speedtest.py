import math
import speedtest

wifi = speedtest.Speedtest()
print("speed")

down_speed = wifi.download()
print(down_speed)
