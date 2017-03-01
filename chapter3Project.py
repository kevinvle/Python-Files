
number = int(input())
collatz(number)

    if (number % 2 == 0):
        print(str(number))
    else if (number % 2 == 1):
        print(str(3 * number + 1))
        return number
    
