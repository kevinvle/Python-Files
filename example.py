import pprint
message = 'It was a bright cold day in April'
count = {}


for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1
        
sometextvariable = pprint.pformat(count)

print(sometextvariable)
