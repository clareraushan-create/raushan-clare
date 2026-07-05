while True:
    try:
        number = int(input("Please enter integer: "))
    except ValueError:
        print("Invalid. Try again.")
        continue
    if number % 2 == 0:
        print("Number is even.")
        break
    else:
        print("Number is odd.")
        break
