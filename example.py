import re # re module which includes all regular expressions

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Create regular expression object stored in phoneNumRegex variable
                                                      # You will usually pass raw strings to re.compile()
                                                      # Backslash doesn't rep \n like next line. \d = looking for a digit. \d 3 = looking for digit 3 times

mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line) # mo nickname for matched object. Also, .search() searches the message for the specific pattern we set in re.compile()')
print = (mo.group()) # method group
