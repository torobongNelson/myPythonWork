from phone_book_menu import PhoneBookMenu
from messages_menu import MessagesMenu
from CallRegisterMenu import CallRegisterMenu
from ToneMenu import ToneMenu


class Nokia:
    def __init__(self):
        self.scanner = input

    def display(self):
        print("Pick a number to choose an action:\n"
              + "1 -----> Phone book\n"
              + "2 -----> Messages\n"
              + "3 -----> Chat\n"
              + "4 -----> Call Register\n"
              + "5 -----> Tones\n"
              + "6 -----> Settings\n"
              + "7 -----> Call Divert\n"
              + "8 -----> Games\n"
              + "9 -----> Calculator\n"
              + "10 -----> Reminders\n"
              + "11 -----> Clock\n"
              + "12 -----> Profiles\n"
              + "13 -----> SIM services\n"
              + ": ")

        user_choice = int(input())

        if user_choice == 1:
            phone_book_menu = PhoneBookMenu()
            phone_book_menu.display()
        elif user_choice == 2:
            messages_menu = MessagesMenu()
            messages_menu.display()
        elif user_choice == 3:
            print("Chat")
        elif user_choice == 4:
            call_register_menu = CallRegisterMenu()
            call_register_menu.display()
        elif user_choice == 5:
            tone_menu = ToneMenu()
            tone_menu.display()
        else:
            print("Invalid choice. Please try again.")

