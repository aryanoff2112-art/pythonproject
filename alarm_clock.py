from playsound import playsound
import time
import os
from datetime import datetime

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds


def alarm(total_seconds):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < total_seconds:
        time.sleep(1)
        time_elapsed += 1

        time_remaining = total_seconds - time_elapsed

        hours_left, minutes_left, seconds_left = format_time(time_remaining)

        if time_remaining <= 10:
            color = RED
        elif time_remaining <= 30:
            color = YELLOW
        else:
            color = GREEN

        print(
            f"{CLEAR_AND_RETURN}"
            f"{color}Time Remaining: "
            f"{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}{RESET}\n",
            end="\r",
            flush=True
        )

    print("\n\n⏰ TIME'S UP! ⏰")
    print("Finished at:", datetime.now().strftime("%I:%M:%S %p"))

    if os.path.exists("alarm.mp3"):
        print("Playing alarm...\n")
        for _ in range(3):
            playsound("alarm.mp3")
    else:
        print("alarm.mp3 not found in this folder.")


def main():
    while True:

        print("=" * 40)
        print("           PYTHON ALARM CLOCK")
        print("=" * 40)

        print("Current Time:", datetime.now().strftime("%I:%M:%S %p"))
        print()

        try:
            hours = int(input("Enter hours   : "))
            minutes = int(input("Enter minutes : "))
            seconds = int(input("Enter seconds : "))

            if hours < 0 or minutes < 0 or seconds < 0:
                print("\nTime cannot be negative.\n")
                continue

            total_seconds = hours * 3600 + minutes * 60 + seconds

            if total_seconds == 0:
                print("\nPlease enter a time greater than 0.\n")
                continue

            print(
                f"\nAlarm set for "
                f"{hours}h {minutes}m {seconds}s"
            )
            print("Alarm will finish at approximately:",
                  (datetime.now()).strftime("%I:%M:%S %p"))

            input("\nPress Enter to start the timer...")

            alarm(total_seconds)

        except ValueError:
            print("\nPlease enter numbers only.\n")
            continue

        again = input("\nDo you want to set another alarm? (y/n): ").lower()

        if again != "y":
            print("\nThank you for using Python Alarm Clock!")
            break

if __name__ == "__main__":
    main()