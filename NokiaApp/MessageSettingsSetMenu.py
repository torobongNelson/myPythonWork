class MessageSettingsSetMenu:
    def __init__(self):
        self.scanner = input

    def display(self):
        print("Set:")
        print("1 -> Message Center number")
        print("2 -> Messages sent as")
        print("3 -> Message Validity")

        choice = int(input())

        if choice == 1:
            print("Message Center number")
        elif choice == 2:
            print("Messages sent as")
        elif choice == 3:
            print("Message Validity")
