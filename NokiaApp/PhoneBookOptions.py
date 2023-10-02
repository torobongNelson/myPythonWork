class PhoneBookOptions:
    def __init__(self):
        self.input = input

    def display(self):
        print("For options:")
        print("1. Type of view")
        print("2. Memory status")

        user_input = int(input())

        if user_input == 1:
            print("Type of view")
        elif user_input == 2:
            print("Memory status")
        else:
            print("Invalid choice. Please try again.")
