from datetime import datetime

def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

weights = []
workouts = []
calories = []

print("Welcome to FitMet Tracker!")

while True:
    print("FITMET DASHBOARD")

    
    print("--------------------------")
    print("\nMenu:")
    print("1. Calculate BMI")
    print("2. Log Weight")
    print("3. View Weight History")
    print("4. Log Workout")
    print("5. View Workout History")
    print("6. Log Calories")
    print("7. View Calorie History")
    print("8. View Weight Statistics")
    print("9. Quit")

    choice = input("Please choose your option (1,9): ")

    if choice == "1":
        try:
            weight = float(input("Please enter your current weight (kg): "))
            height = float(input("Please enter your current height (cm): "))
            bmi = calculate_bmi(weight, height)
        except ValueError:
            print("Invalid values, try again.")
            continue
        finally:
            print("Values stored... calculating.")
        
        if bmi < 18.5:
            category = "underweight"
        elif 18.6 < bmi < 24.9:
            category = "normal weight"
        elif 25 < bmi < 29.9:
            category = "overweight"
        else:
            categort = "obese"

        print(f"Your BMI is {bmi:.2f} which makes you {category}.")

    elif choice == "2":
        try:
            weight = float(input("Please enter your current weight (kg): "))
        except ValueError:
            print("Invalid value. Try again.")
            continue
        print("Weight stored successfully.")
        weights.append({
            "weight": weight,
            "date": datetime.now().strftime("%d,%m,%y")
        })

    elif choice == "3":
        if weights:
            print("\nWeight History:")
            for i, w in enumerate(weights, start = 1):
                print(f"{i}, {w} kg")
        else:
            print("No data available.")

    elif choice == "4":
        workout = input('Enter type of workout: ')
        try:
            duration = int(input("Enter duration of workout (min): "))
        except ValueError:
            print("Invalid input.")
            continue
        finally:
            print("Workout stored")
        workouts.append({
            'workout': workout,
            'duration': duration,
        })

    elif choice == "5":
        if workouts:
            print("\nWorkout History:")
            for i, w in enumerate(workouts, start = 1):
                print(f"{i}, {w}")
        else:
            print("No data available")


    elif choice == "6":
        try:
            calorie = int(input("Enter calorie intake: "))
        except ValueError:
            print("Invalid response. Try again.")
            continue
        print("Stored successfully.")
        calories.append({
            'calorie': calorie,
            'date': datetime.now().strftime("%d,%m,%y")
        })
    
    elif choice == "7":
        if calories:
            print("\nCalorie History:")
            for i, w in enumerate(calories, start = 1):
                print(f"{i}, {w} calories")
        else:
            print("No data available.")
    
    elif choice == "8":
        
        weight_values = [entry["weight"] for entry in weights]

        if weights:
            print("Weight Stats:")
            print("Current Weight:", weight_values[-1])
            print("Highest Weight:", max(weight_values))
            print("Lowest Weight:", min(weight_values))
            print("Average Weight:", sum(weight_values) / len(weight_values))

        else:
            print("No data available.")

    elif choice == "9":
        print("Thank you for using FitMet tracker!")
        break