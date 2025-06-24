# # Avoid Repeated Content is Sets

# s = {2, 5, 6, 5}
# print(s)

# # Quick Quiz
# shiv = set()
# print(type(shiv))



# Methods Of Sets in Python

s1 = {3, 2, 7, 4}
s2 = {5, 7,1}
print(s1.union(s2))             #   <------- Do not Repeat Value Of Both S1&S2
print(s1.intersection(s2))      #   <------- Common Value From Both set
print(s1.difference(s2))        #   <------- Same as intersection Tag