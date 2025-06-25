# # For accesing a text in another files!!
# f = open('myfile.txt')
# text = f.read()
# print(text)
# f.close()


# For Adding text in file u can use append.
f = open('myfile.txt', 'a')
f.write("Hello world!")
print(f)