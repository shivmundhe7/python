import random
import time
import sys

password = input("Send the password: ")
chars = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
password_length = len(password)
tries = 0

print("Cracking password... Please wait.\n")

while True:
    attempt = [random.choice(chars) for _ in range(password_length)]
    tries += 1
    attempt_str = "".join(attempt)
    
    sys.stdout.write(f"\rTrying: {attempt_str} | Attempts: {tries}")
    sys.stdout.flush()
    
    time.sleep(0.01)  # Delay for animation effect (lower = faster)

    if attempt_str == password:
        break

print(f"\n\n✅ Password cracked: {attempt_str} in {tries} attempts.")
