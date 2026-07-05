import random
while True:
    number = random.randint(1, 6)


    while True:
        try:
            user_guess = int(input('Enter your guess (1,6): '))
            if user_guess == number:
                print('Well done you got it right.')
            else:
                print(f"Incorrect, answer was {number}.")
                
        except ValueError:
            print("Invalid entry.")
            continue

        choice = input("Do you want to do again (y/n): ").lower()
        if choice != 'y':
            break
        