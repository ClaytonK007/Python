#
#   Create a BMI calculator. Allow users to choose metric (kgs and meters or lbs and inches).
#
while True:
    print("BMI Calculator")
    print("-"*14)
    print("1. Kgs and Meters\n2. Lbs and inches\n3. Exit")
    try:
        opt = int(input("Select option: "))
    except ValueError:
        print("Invalid option. Please try again.")

    if opt == 1:
        try:
            def bmi(weight, height):
                return weight / (height ** 2)
        
            weight = float(input("Enter weight in Kgs: "))
            height = float(input("Enter height in meters: "))

            bmi_1 = bmi(weight, height)
            print("-"*14)
            print(f"Your BMI is {bmi_1:.2f}.")

            if bmi_1 < 18.5:
                print("You are underweight.")
            elif 18.5 <= bmi_1 < 25:
                print("You are in healthy weight range.")
            elif 25 <= bmi_1 < 30:
                print("You are overweight.")
            else:
                print("You are obese.")
        except ValueError:
            print("Invalid input. Please insert numeric values.")
        print("-"*14)
    elif opt == 2:
        try:
            def bmi(weight, height):
                return (weight / (height ** 2)) * 703

            weight = float(input("Enter weight in Lbs: "))
            height = float(input("Enter height in inches: "))

            bmi_2 = bmi(weight, height)
            print("-"*14)
            print(f"Your BMI is {bmi_2:.2f}.")

            if bmi_2 < 18.5:
                print("You are underweight.")
            elif 18.5 <= bmi_2 < 25:
                print("You are in healthy weight range.")
            elif 25 <= bmi_2 < 30:
                print("You are overweight.")
            else:
                print("You are obese.")
        except ValueError:
            print("Invalid input. Please insert numeric values.")
        print("-"*14)
    elif opt == 3:
        break
    else:
        print("Invalid option. Please select valid option.")