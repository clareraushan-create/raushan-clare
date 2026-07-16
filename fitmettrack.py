import json
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import re 

def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2


def save_data():
    data = {
        "weights": weights,
        "workouts": workouts,
        "calories": calories,
        "bmis": bmis
    }
    with open("fitmet_data.json", "w") as file:
        json.dump(data, file, indent=4)

try:
    with open("fitmet_data.json", 'r') as file:
        data = json.load(file)

        weights = data.get("weights", [])
        workouts = data.get("workouts", [])
        calories = data.get("calories", [])
        bmis = data.get("bmis", [])
except FileNotFoundError:
    weights = []
    workouts = []
    calories = []
    bmis = []
FILENAME = "password_data.json"
def save_password():
    
    user_password = input("Enter your password to store: ")
    data = {
        "password": user_password
    }
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Password stored successfully!\n")

while True:
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)

        password = data.get("password")
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            user_guess = input("Login: Enter password: ")

            if user_guess == password:
                print("Login Successful!")
                break
            else:
                attempts += 1
                remaining = max_attempts - attempts
                print(f"Incorrect. Attempts remaining: {remaining}")

        if attempts == max_attempts:
            print("Account locked...")
            break
        break
        
    except FileNotFoundError:
        print("No password file found. Lets create one.")
        save_password()

            
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
    print("9. View BMI History")
    print("10. Quit")

    choice = input("Please choose your option (1,10): ")

    if choice == "1":
        add_or_remove = input("Do you want to add or remove values (add/remove): ").lower()
        if add_or_remove == "add":
            try:
                weight = float(input("Please enter your current weight (kg): "))
                height = float(input("Please enter your current height (cm): "))
                bmi = calculate_bmi(weight, height)
                bmis.append({
                    "bmi": bmi,
                    "date": datetime.now().strftime("%d,%m,%y")
                })
                save_data()
            except ValueError:
                print("Invalid values, try again.")
                continue
            else:
                print("Values stored... calculating.")
            
            if bmi < 18.5:
                category = "underweight"
            elif bmi < 25:
                category = "normal weight"
            elif bmi < 30:
                category = "overweight"
            else:
                category = "obese"

            print(f"Your BMI is {bmi:.2f} which makes you {category}.")
        elif add_or_remove == "remove":
            try:
                bmi_to_remove = float(input("What value do you want to remove: "))
                found = False
                for entry in bmis:
                    if entry["bmi"] == bmi_to_remove:
                        bmis.remove(entry)
                        save_data()
                        print(f"Removed {bmi_to_remove}")
                        found = True
                        break
                if not found:
                    print("No value in database.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "2":
        add_or_remove = input("Do you want to add or remove values (add/remove): ").lower()
        if add_or_remove == "add":
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
            save_data()
        elif add_or_remove == "remove":
            try:
                weight_to_remove = float(input("What weight value do you want to remove: "))
                found = False
                for entry in weights:
                    if entry["weight"] == weight_to_remove:
                        weights.remove(entry)
                        save_data()
                        print(f"Removed {weight_to_remove} kg.")
                        found = True
                        break
                if not found:
                    print("Weight not found in database.")
            except ValueError:
                print("Please enter a valid number")
          
        
    elif choice == "3":
        if weights:
            print("\nWeight History:")
            for i, w in enumerate(weights, start = 1):
                print(f"{i}. {w['weight']} kg ({w['date']}])")
            y = np.array([w["weight"] for w in weights])
            x = np.array([w["date"] for w in weights])
            font1 = {'family':'serif', 'color':'blue', 'size':18}
            font2 = {'family':'serif', 'color':'darkred', 'size':15}
            plt.plot(x, y, 'r')
            plt.ylabel("Weight (kg)", fontdict = font2)
            plt.xlabel("Date", fontdict = font2)
            plt.title("Weight Progress", fontdict = font1)
            plt.grid(True)
            plt.show()
            
        else:
            print("No data available.")

    elif choice == "4":
        workout = input('Enter type of workout: ')
        try:
            duration = int(input("Enter duration of workout (min): "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            print("Workout stored")
        workouts.append({
            'workout': workout,
            'duration': duration,
        })
        save_data()

    elif choice == "5":
        if workouts:
            print("\nWorkout History:")
            for i, w in enumerate(workouts, start = 1):
                print(f"{i}. {w['workout']} - {w['duration']} mins")
        else:
            print("No data available")


    elif choice == "6":
        add_or_remove = input("Do you want to add or remove values (add/remove): ").lower()
        if add_or_remove == "add":
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
            save_data()
        elif add_or_remove == "remove":
            try:
                calorie_to_remove = float(input("What value do you want to remove: "))
                found = False
                for entry in calories:
                    if entry["calorie"] == calorie_to_remove:
                        calories.remove(entry)
                        save_data()
                        print(f"Removed {calorie_to_remove} cal.")
                        found = True
                        break
                if not found:
                    print("No value in database.")
            except ValueError:
                print("Please enter a valid number")
    
    elif choice == "7":
        if calories:
            print("\nCalorie History:")
            for i, w in enumerate(calories, start = 1):
                print(f"{i}. {w['calorie']} calories ({w['date']})")
            y = np.array([w["calorie"] for w in calories])
            x = np.array([w["date"] for w in calories])
            font1 = {'family':'serif', 'color':'blue', 'size':18}
            font2 = {'family':'serif', 'color':'darkred', 'size':15}
            plt.plot(x, y, 'r')
            plt.ylabel("Calories", fontdict = font2)
            plt.xlabel("Date", fontdict = font2)
            plt.title("Calorie Intake", fontdict = font1)
            plt.grid(True)
            plt.show()
            
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
        if bmis:
            print("\nBMI History:")
            for i, w in enumerate(bmis, start = 1):
                print(f"{i}. {w['bmi']:.2f} ({w['date']})")
            y = np.array([w["bmi"] for w in bmis])
            x = np.array([w["date"] for w in bmis])
            font1 = {'family':'serif', 'color':'blue', 'size':18}
            font2 = {'family':'serif', 'color':'darkred', 'size':15}
            plt.plot(x, y, 'r')
            plt.ylabel("BMI", fontdict = font2)
            plt.xlabel("Date", fontdict = font2)
            plt.title("BMI Progress", fontdict = font1)
            plt.grid(True)
            plt.show()
        else:
            print("No history available. ")

    elif choice == "10":
        print("Thank you for using FitMet tracker!")
        break

