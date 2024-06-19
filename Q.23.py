def convert_temperature():
    choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().lower()
    temp = float(input("Enter the temperature: "))
    if choice == 'c':
        print(f"{temp} Celsius is {(temp * 9/5) + 32} Fahrenheit.")
    elif choice == 'f':
        print(f"{temp} Fahrenheit is {(temp - 32) * 5/9} Celsius.")
    else:
        print("Invalid choice.")

convert_temperature()