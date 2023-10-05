class Clock:
    def display(self):
        print("1. Alarm Clock")
        print("2. Clock settings")
        print("3. Date settings")
        print("4. Stop watch")
        print("5. Countdown time")
        print("6. Auto update of date and time")

        user_input = int(input("Enter your choice: "))

        match user_input:
            case 1:
             print("Alarm Clock")
            case 2:
             print("Clock settings")
            case 3:
             print("Date settings")
            case 4:
             print("Stop watch")
            case 5:
             print("Countdown time")
            case 6:
             print("Auto update of date and time")
            case _:
             print("Invalid option chosen")
