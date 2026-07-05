while True:
    try:
        number = int(input("Enter your integer: "))
    except ValueError:
        print("Integer invalid try again.")
        continue

    for i in range(1, 11):
        print(number * i)

    choice = input("Do you want to do again (y/n): ").lower()
    if choice != 'y':
        break
    else:
        continue