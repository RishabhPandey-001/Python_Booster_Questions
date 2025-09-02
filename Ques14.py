# 14.	Angle Between Clock Hands: Find the angle between hour and minute hands.
# Every hour the hour hand moves 30 degrees (360° / 12 = 30°).
# Every minute the minute hand moves 6 degrees (360° / 60 = 6°).
# The hour hand also slightly moves each minute (0.5° per minute)
import math
def Clock_Angle(Hour, Minute):
    Hour = Hour % 12
    Hour_angle = (Hour * 30) + (Minute * 0.5)
    Minute_angle = Minute * 6

    angle = abs(Hour_angle - Minute_angle)    
    angle = min(angle, 360 - angle)
    return angle
try:
    Hour = int(input("Enter the hour from 0 - 23: "))
    Minute = int(input("Enter the Minute: "))
    if 0 <= Hour <= 23 and 0 <= Minute <= 59:
        result = Clock_Angle(Hour, Minute)
        print(f"The angle between clock hands is {result} degrees.")
    else:
        print("Please enter valid hour (0-23) and minute (0-59) values.")
except ValueError:
    print("Invalid input! Please enter integer values only.")
