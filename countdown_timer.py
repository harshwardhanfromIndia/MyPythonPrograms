import time

my_timer = int(input("Enter time in seconds: "))

for t in range(my_timer, 0, -1):
    seconds = t % 60
    minutes = int(t / 60) % 60
    hours = int(t / 3600)
    print(f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIMES UP!")