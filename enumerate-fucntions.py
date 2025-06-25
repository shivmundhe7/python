marks = [12, 56, 23 ,17, 98]
# index = 0
# for marks in marks:
#       print(index,marks)
#     if(index == 4):
#         print("Awesome Shiv")
#     index +=1


# Now We will make using  enumerate Function

index = 0
for index, marks in enumerate(marks):     #<------------ here is enumerate function
    print(index,marks)
    if(index == 4):
        print("Awesome shiv")
    index +=1
