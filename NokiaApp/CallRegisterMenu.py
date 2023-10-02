
from ShowCallDurationMenu import ShowCallDurationMenu
class CallRegisterMenu:
    def __init__(self):
        self.scanner = input

    def display(self):
        print("Call Register:")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialed numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")

        choice = int(input())

        if choice == 1:
            print("Missed calls")
        elif choice == 2:
            print("Received calls")
        elif choice == 3:
            print("Dialed numbers")
        elif choice == 4:
            print("Erase recent call lists")
        elif choice == 5:
            show_call_duration_menu = ShowCallDurationMenu()
            show_call_duration_menu.display()
