#
#   Create a unit coverter. Allow users to choose metric (kms to miles,  miles to kms,
#   kilograms to pounds or pounds to kilograms).
#
def k_to_m(km):
    return km * 0.621371

def m_to_k(m):
    return m * 1.60934

def kg_to_lbs(kg):
    return kg * 2.205

def lbs_to_kg(lbs):
    return lbs / 2.205 

while True:
    print("Unit Converter")
    print("-"*14)
    print("1. Kms to Miles\n2. Miles to Kms\n3. Kgs to Lbs\n4. Lbs to Kgs\n5. Exit")
    try:
        opt = int(input("Enter choice: "))
    except ValueError:
        print("Invalid option. Please try again.")

    try:
        if opt == 1:
            km = float(input("Enter distance in Kms: "))
            print(f"Distance in Miles: {k_to_m(km):.2f}")
            print("-"*14)
        elif opt == 2:
            m = float(input("Enter distance in miles: "))
            print(f"Distance in Kilometers: {m_to_k(m):.2f}")
            print("-"*14)
        elif opt == 3:
            kg = float(input("Enter weight in Kilograms: "))
            print(f"Weight in pounds: {kg_to_lbs(kg):.2f}")
            print("-"*14)
        elif opt == 4:
            lbs = float(input("Enter weight in pounds: "))
            print(f"Weight in Kilograms: {lbs_to_kg(lbs):.2f}")
            print("-"*14)
        elif opt == 5:
            break
        else: 
            print("Incorrect option. Please choose valid option.")
    except ValueError:
        print("Incorrect option. Please choose valid option.")