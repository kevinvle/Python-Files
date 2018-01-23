def isPhoneNumber(text): # Function checks if input is a standard phone number
    if len(text) != 12:
        return False # Check if text is the correct phone# size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # Missing dash
        if text[3] != '-':
            return False # Checks if phone# has dash
        for i in range (4, 7):
            if not text[i].isdecimal():
                return False # Checks 2nd part of phone# is dec.
        if text[7] != '-':
            return False # Missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # Checks if last 4 digits are dec.
    return True # True if we have our correct phone number)

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
foundNumber = False # Will set this to true later on if it is correct.

for i in range(len(message)):
    chunk = message[i:i+12] # Every 12 character long chunk from the big string (message). Using a slicer for this
    # When i=0, it'll grab the first 12 characters starting at 'C' When i=1 it'll grab the next 12 characters starting at 'a'.
    # We want 12 char's because it's the length of our phone number.
    if isPhoneNumber(chunk):
        print('Phone number found ' + chunk)
        foundNumber = True
if not foundNumber: # If foundNumber isn't true
    print('Could not find any phone numbers.')
    
