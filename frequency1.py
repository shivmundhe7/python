def count_char(name):
    for char in set(name):
        print(f"{char} = {name.count(char)}")
name = input("Enter your name: ")
count_char(name)

if len(name) % 2 != 0:
    print()("This is an odd number")
else:
    print("This is an even number")