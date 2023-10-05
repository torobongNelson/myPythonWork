from ShowCallDurationMenu import ShowCallDurationMenu


class CallRegisterMenu:

    def display(self):
        print("Call Register:")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialed numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")

        choice = int(input())
        match choice:
            case 1:
                print("Missed calls")
            case 2:
                print("Received calls")
            case 3:
                print("Dialed numbers")
            case 4:
                print("Erase recent call lists")
            case 5:
                show_call_duration_menu = ShowCallDurationMenu()
                show_call_duration_menu.display()
