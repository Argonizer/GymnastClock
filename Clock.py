import datetime

def clamp(val, min, max):
    if(val > max):
        return max
    elif(val < min):
        return min
    return val

def roundOffAngle(angle):
    if angle < 0:
        angle += 360
    elif angle >= 360:
        angle -= 360
    return angle

def getTime():
    time = datetime.datetime.now()
    return time


def getHourAngle():
    now = getTime()
    hour = now.hour
    if(hour > 12):
        hour -= 12
    hourAngle = hour * 30 - 90
    hourAngle = roundOffAngle(hourAngle)
    return hourAngle

def getMinuteAngle():
    now = getTime()
    minute = now.minute
    minuteAngle = minute * 6 - 90
    minuteAngle = 360 - roundOffAngle(minuteAngle)
   # print(minuteAngle,"          ",minute)
    return minuteAngle

def getSecondAngle():
    now = getTime()
    second = now.second
    micros = now.microsecond

    secondAngle = second * 6 - 90 + int(micros/100000*0.6)
    secondAngle = 360 - roundOffAngle(secondAngle)
    print(secondAngle,"         ",second)
    return secondAngle


