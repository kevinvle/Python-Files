import re # re module which includes all regular expressions

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Create regular expression object stored in phoneNumRegex variable
                                                      # You will usually pass raw strings to re.compile()
                                                      # Backslash doesn't rep \n like next line. \d is the regex for a numeric digit character. \d 3 = looking for digit 3 times
                                                      # Calling re.compile function to create a regex object 
print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line) # mo nickname for matched object. Also, .search() searches the message for the specific pattern we set in re.compile()'))
#print = (mo.group()) # match object (nickname) group's method 

# If you want to find multiple numbers, .findall() method instead of .search() and comment out print mo group. Also remove mo variable
