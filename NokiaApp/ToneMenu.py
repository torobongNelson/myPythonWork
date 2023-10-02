class ToneMenu:
    def __init__(self):
        self.scanner = input

    def display(self):
        print("Tones")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Composer")
        print("5. Message alert tone")
        print("6. Keypad tones")
        print("7. Warning and game tones")
        print("8. Vibrating alert")
        print("9. Screen saver")

        choice = int(input())

        if choice == 1:
            print("Ringing tone")
        elif choice == 2:
            print("Ringing volume")
        elif choice == 3:
            print("Incoming call alert")
        elif choice == 4:
            print("Composer")
        elif choice == 5:
            print("Message alert tone")
        elif choice == 6:
            print("Keypad tones")
        elif choice == 7:
            print("Warning and game tones")
        elif choice == 8:
            print("Vibrating alert")
        elif choice == 9:
            print("Screen saver")
