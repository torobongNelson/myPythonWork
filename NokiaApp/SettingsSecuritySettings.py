class SettingsSecuritySettings:
    def display(self):
        print("1. PIN code request:")
        print("2. Call barring service")
        print("3. Fixed dialling")
        print("4. Closed user group")
        print(" 5. Phone security")
        print("6. Change access code")

        user_input = int(input("choose an option"))

        match user_input:
            case 1:
                print(" PIN code request:")
            case 2:
                print(" Call barring service")
            case 3:
                print(". Fixed dialling")
            case 4:
                print(" Closed user group")
            case 5:
                print(" Phone security")
            case 6:
                print("Change access code")
