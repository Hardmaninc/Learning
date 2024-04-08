# timer count down allowing user to put in a number in mins to count down from.

import time

def main():
    timer_start = input("Please put a number in minutes to count down from \n")
    timer = int(timer_start)
    while timer > 0:
        print(timer)
        time.sleep(60)
        timer -= 1
        if timer == 0:
            print("Time is up!")


main()