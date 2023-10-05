class SettingsPhoneSettings:
    def display(self):
        print("1. Language")
        print("2. Cell info display")
        print("3. Welcome note")
        print("4. Network selection")
        print("5. Lights")
        print("6. Confirm SIM service action")

        user_input = input("Enter your choice: ")

        try:
            user_input = int(user_input)
            if user_input == 1:
                print("Language")
            elif user_input == 2:
                print("Cell info display")
            elif user_input == 3:
                print("Welcome note")
            elif user_input == 4:
                print("Network selection")
            elif user_input == 5:
                print("Lights")
            elif user_input == 6:
                print("Confirm SIM service action")
            else:
                print("Invalid option chosen")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

