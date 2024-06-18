print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('PYTHON PROJECT 4 - MEASUREMENT CONVERTER')
print()
print()

def show_menu():
    print("Measurement Converter Menu:")
    print("A. Millimeters to Centimeters")
    print("B. Centimeters to Meters")
    print("C. Feet to Meters")
    print("D. Inches to Centimeters")
    print("E. Miles to Kilometers")
    print("F. Exit")


def mm_to_cm(mm):
    return mm / 10.0


def cm_to_m(cm):
    return cm / 100.0


def ft_to_m(ft):
    return ft * 0.3048


def inches_to_cm(inches):
    return inches * 2.54


def miles_to_km(miles):
    return miles * 1.60934


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (A-F): ")

        if choice == 'A':
            mm = float(input("Enter length in millimeters: "))
            cm = mm_to_cm(mm)
            print(f"{mm} mm = {cm} cm\n")
        elif choice == 'B':
            cm = float(input("Enter length in centimeters: "))
            m = cm_to_m(cm)
            print(f"{cm} cm = {m} m\n")
        elif choice == 'C':
            ft = float(input("Enter length in feet: "))
            m = ft_to_m(ft)
            print(f"{ft} ft = {m} m\n")
        elif choice == 'D':
            inches = float(input("Enter length in inches: "))
            cm = inches_to_cm(inches)
            print(f"{inches} inches = {cm} cm\n")
        elif choice == 'E':
            miles = float(input("Enter length in miles: "))
            km = miles_to_km(miles)
            print(f"{miles} miles = {km} km\n")
        elif choice == 'F':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a letter from A to F.\n")


if __name__ == "__main__":
    main()
