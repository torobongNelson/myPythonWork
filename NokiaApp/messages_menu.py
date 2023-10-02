from MessageSettingsMenu import MessageSettingsMenu


class MessagesMenu:
    def __init__(self):
        self.scanner = input

    def display(self):
        print("Messages:")
        print("1 -> Write messages")
        print("2 -> Inbox")
        print("3 -> Outbox")
        print("4 -> Picture messages")
        print("5 -> Templates")
        print("6 -> Smileys")
        print("7 -> Message setting")
        print("8 -> Info service")
        print("9 -> Voice mailbox number")
        print("10 -> Service command editor")

        choice = int(input())

        if choice == 1:
            print("Write messages")
        elif choice == 2:
            print("Inbox")
        elif choice == 3:
            print("Outbox")
        elif choice == 4:
            print("Picture messages")
        elif choice == 5:
            print("Templates")
        elif choice == 6:
            print("Smileys")
        elif choice == 7:
            message_settings_menu = MessageSettingsMenu()
            message_settings_menu.display()
        elif choice == 8:
            print("Info service")
        elif choice == 9:
            print("Voice mailbox number")
        elif choice == 10:
            print("Service command editor")
