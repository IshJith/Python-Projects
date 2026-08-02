import time
import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Wooden Train Whistle.mp3"

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS)")
    set_alarm(alarm_time)
    is_Running = True

    while is_Running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake up")
            is_Running = False
            

        time.sleep(1)