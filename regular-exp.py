import re

text = "My phone number is 24624624626"
match = re.search(r"\d{10}", text)
print(match.group())

# Email Finder


text = "Contact me at shivmundhe16@gmail.com"
email = re.search(r"\w+@\w+\.\w+", text)

print(email.group())

