#
#   Create a temperature converter. Allow users to choose which temperature scale (C or F).
#
def c_to_f(num):
    return (num * 9/5) + 32

def f_to_c(num):
    return (num - 32) * 5/9

while True:
    try:
        choice = input("Convert to C or F: ").upper()
        temp = float(input("Enter temperature: "))

        if choice == "C":
            print(f"Temperature to Celcius: {f_to_c(temp):.2f}°C")
        elif choice == "F":
            print(f"Temperature to Fahrenheit: {c_to_f(temp):.2f}°F")
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Please enter a valid numeric temperature.")
