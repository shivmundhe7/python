# dic = {
#     "Shiv" : "Human Being",
#     "Spoon" : "Object"
# }

# print(dic["Shiv"])
# print(dic.get('Shiv'))
# print(dic.keys())

# for key in dic.keys():
#     print(f"The Value Corresponding to the key {key} is {dic[key]}")

# Methods of dictionary methods

ep1 = {122:45 , 143:34 , 341:56, 183:89}
ep2 = {222:34, 142:45}
ep1.update(ep2)  #Combines Both Values 
ep1.popitem()    #it Deletes last entry 
ep1.clear()
print(ep1)