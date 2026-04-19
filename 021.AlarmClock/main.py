import datetime
import time
import pygame

pygame.mixer.init()

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}...")
    alarm_condition = True
    sound = pygame.mixer.Sound("iphone_alarm.mp3")

    while alarm_condition:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {now}")

        if now == alarm_time:
            print("\n---- WAKE UP! ----")
            sound.play()
            alarm_condition = False
            time.sleep(15)

        time.sleep(1)


if __name__ == '__main__':
    target_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(target_time)
