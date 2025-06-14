import time

def get_total_seconds(days, hours, minutes, seconds):
    return days * 86400 + hours * 3600 + minutes * 60 + seconds

def countdown_timer(total_seconds):
    while total_seconds > 0:
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        timer = f'{days:02d}d:{hours:02d}h:{minutes:02d}m:{seconds:02d}s'
        print(timer, end='\r')  # You can replace with print(timer) if it causes issues
        time.sleep(1)
        total_seconds -= 1
    print("\nTime's up!")

if __name__ == "__main__":
    try:
        days = int(input("Enter days: "))
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))

        total_time = get_total_seconds(days, hours, minutes, seconds)
        countdown_timer(total_time)

    except ValueError:
        print("Please enter valid integers for time.")
