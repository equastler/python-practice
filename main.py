count = 1
while count < 101:
    if count%15 == 0:
        print("FizzBuzz")
        count += 1
    elif count%3 == 0:
        print("Fizz")
        count += 1
    elif count%5 == 0:
        print("Buzz")
        count += 1
    else:
        print(count)
        count += 1

