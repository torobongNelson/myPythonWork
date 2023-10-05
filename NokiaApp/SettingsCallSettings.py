class SettingsCallSettings:
    def display(self):
        print("1. Automatic redial")
        print("2. Speed dialing")
        print("3. Call waiting option")
        print("4. Own number sending")
        print("5. Phone line in use")
        print("6. Automatic answer")

        user_input = int(input("Enter your choice: "))

        match user_input:
            case 1:
                print("Automatic redial")
            case 2:
                print("Speed dialing")
            case 3:
                print("Call waiting option")
            case 4:
                print("Own number sending")
            case 5:
                print("Phone line in use")
            case 6:
                print("Automatic answer")
            case _:
                print("Invalid option chosen")
