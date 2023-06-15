import math
import speedtest

wifi = speedtest.Speedtest()

down_speed = wifi.download()
print("Speed of downloading", down_speed)
up_speed = wifi.upload()
print("Speed of uploading", up_speed)
