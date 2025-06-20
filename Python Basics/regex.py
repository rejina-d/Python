#regex in Python
import re

#pattern for regex
# pattern = r'[a-z]'
# string = "a"

#pattern for regex
pattern = "This"
string = "This is a test string"

# #matching the pattern in the string
# search_string = re.search(pattern, string)
# print(search_string)

# match_string = re.match(pattern, string)
# print(match_string)


# #matching the pattern in the string
if re.match(pattern, string):
    print("Match found")
    
#search
if re.search(pattern, string):
    print("Search found")
    
pattern = r'[A-Z]+[a-z]+\d'
string = input("Enter String:")

if re.match(pattern, string):
    print("Match found")
else:
    print("Match not found")
    
pattern = r'[A-Za-z0-9]+@+[A-Za-z]+\.[A-Za-z]'
string = input("Enter your email:")
if re.match(pattern, string):
    print("Valid Email")
    print("Signup successfully")
else:
    print("Invalid email")