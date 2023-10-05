from phone_book_menu import PhoneBookMenu
from messages_menu import MessagesMenu
from CallRegisterMenu import CallRegisterMenu
from ToneMenu import ToneMenu
from Settings import Settings
from Clock import Clock


class Nokia:

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

        elif user_choice == 6:
            settings = Settings()
            settings.display()

        elif user_choice == 7:
            print("Call divert")

        elif user_choice == 8:
            print("games")

        elif user_choice == 9:
            print("calculator")

        elif user_choice == 10:
            print("Reminder")

        elif user_choice == 11:
            clock = Clock()
            clock.display()

        elif user_choice == 12:
            print("profiles")

        elif user_choice == 13:
            print("SIM services")

        else:
            print("Invalid choice. Please try again.")
