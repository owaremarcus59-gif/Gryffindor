import winsound
import time

def beep_alarm():
    for repeats in range(7):
        winsound.beep(3000, 500)
        winsound.beep(6000, 300)


timerDuration = 6

hours, minutes, second = 0, 0, 0
for i in range(timerDuration):
    print('\n' * 100)

    second += 1
    if second == 60:
        minutes += 1
        second = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    print(str(hours) + ':' + str(minutes) + ':' + str(second))
    time.sleep(1)

if __name__ == '__main__':
    beep_alarm()
        
           