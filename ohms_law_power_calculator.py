
# OHM'S LAW AND POWER CALCULATOR
# CTE123 Python Mini Project

# Stores previous calculations.
calculation_history = []


# Function for collecting valid numerical input.
def get_number(message, allow_zero=True):
    while True:
        try:
            number = float(input(message))

            if number < 0:
                print("Negative values are not allowed.")

            elif not allow_zero and number == 0:
                print("This value cannot be zero.")

            else:
                return number

        except ValueError:
            print("Invalid input. Please enter a number.")


# Displays the calculator menu.
def show_menu():
    print("\n===== OHM'S LAW AND POWER CALCULATOR =====")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. View Calculation History")
    print("0. Exit")


# Performs electrical calculations.
def calculate(choice):

    if choice == 1:
        current = get_number("Enter current (A): ")
        resistance = get_number("Enter resistance (Ohms): ", False)

        voltage = current * resistance
        power = voltage * current

    elif choice == 2:
        voltage = get_number("Enter voltage (V): ")
        resistance = get_number("Enter resistance (Ohms): ", False)

        current = voltage / resistance
        power = voltage * current

    elif choice == 3:
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ", False)

        resistance = voltage / current
        power = voltage * current

    elif choice == 4:
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")

        power = voltage * current

        if current == 0:
            resistance = None
        else:
            resistance = voltage / current

    else:
        return

    # Feature 1: Display complete circuit summary.
    print("\n===== CIRCUIT SUMMARY =====")
    print(f"Voltage: {voltage:.2f} V")
    print(f"Current: {current:.2f} A")

    if resistance is None:
        print("Resistance: Undefined")
    else:
        print(f"Resistance: {resistance:.2f} Ohms")

    print(f"Power: {power:.2f} W")

    # Feature 2: Save calculation history.
    summary = (
        f"Voltage={voltage:.2f}V, "
        f"Current={current:.2f}A, "
        f"Resistance={resistance if resistance is not None else 'Undefined'}, "
        f"Power={power:.2f}W"
    )

    calculation_history.append(summary)


# Main program.
def main():

    while True:
        show_menu()

        try:
            choice = int(input("Choose an option: "))

            if choice == 0:
                print("Thank you for using the calculator.")
                break

            elif choice in [1, 2, 3, 4]:
                calculate(choice)

            elif choice == 5:
                print("\n===== CALCULATION HISTORY =====")

                if len(calculation_history) == 0:
                    print("No calculations recorded yet.")
                else:
                    for item in calculation_history:
                        print(item)

            else:
                print("Invalid option. Select between 0 and 5.")

        except ValueError:
            print("Please enter a valid menu number.")


# Starts the application.
if __name__ == "__main__":
    main()
      
