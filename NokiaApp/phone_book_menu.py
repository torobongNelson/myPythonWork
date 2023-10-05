from PhoneBookOptions import PhoneBookOptions


class PhoneBookMenu:
    def display(self):
        print("Phone Book Menu:")
        print("1. Search")
        print("2. Service Nos. 1")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b’card")
        print("8. Options")
        print("9. Speed dials")
        print("10. Voice tags")

        user_input = int(input())

        if user_input == 1:
            print("Search")
        elif user_input == 2:
            print("Service Nos. 1")
        elif user_input == 3:
            print("Add name")
        elif user_input == 4:
            print("Erase")
        elif user_input == 5:
            print("Edit")
        elif user_input == 6:
            print("Assign tone")
        elif user_input == 7:
            print("Send b’card")
        elif user_input == 8:
            phone_book_options = PhoneBookOptions()
            phone_book_options.display()
        elif user_input == 9:
            print("Speed dials")
        elif user_input == 10:
            print("Voice tags")
        else:
            print("Invalid choice. Please try again.")

# You would need to define the PhoneBookOptions class separately with its display method.
