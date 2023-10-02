from MessageSettingsSetMenu import MessageSettingsSetMenu
class MessageSettingsMenu:
    def __init__(self):
        self.scanner = input

    def display(self):
        print("Message settings")
        print("""
              1. set
              2. common
              """)

        choice = int(input())

        if choice == 1:
            message_settings_set_menu = MessageSettingsSetMenu()
            message_settings_set_menu.display()
        elif choice == 2:
            message_settings_common_menu = MessageSettingsCommonMenu()
            message_settings_common_menu.display()
