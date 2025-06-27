import time
print(time.time())

# Time sleep 
print("Wait for 3 seconds...")
time.sleep(3)
print("Done!")

# Localtime
print(time.localtime())


# Execution Time
start = time.time()
time.sleep(2)
end = time.time()

print("Program took", end - start, "seconds")
