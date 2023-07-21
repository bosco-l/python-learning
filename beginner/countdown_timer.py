import time


def countdown(s: int):
    while s:
        hours, mins = divmod(int(s / 60), 60)
        _, secs = divmod(s, 60)
        print(f"{hours}:{mins:02}:{secs:02}", end="\r")  # carriage return
        time.sleep(1)
        s -= 1


if __name__ == '__main__':
    s = input("Enter the time in seconds:")
    countdown(int(s))
