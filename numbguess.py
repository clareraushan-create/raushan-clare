import random 
number = random.randint(1,10)
print(number)
while True:
    try:
        user_guess = int(input("Enter your guess (1,10): "))
    except ValueError:
        print("Invalid input. Try again.")
        continue

    if user_guess == number:
        print("Correct. You win!")
        break
    
    elif user_guess > number:
        print("Too high. Try again.")
        continue

    elif user_guess < number:
        print("Too low. Try again.")
        continue
    


        
