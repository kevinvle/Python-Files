def spam():
    global eggs
    eggs = 'hi'
    print(eggs)

eggs = 42
spam()
print(eggs)
