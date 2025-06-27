import time
from plyer import notification

def remind_water():
    while True:
        notification.notify(
            title="💧 Drink Water Reminder",
            message="Time to drink a glass of water!",
            timeout=5
        )
        print("Reminder sent!")
        time.sleep(10)  
remind_water()
