from SettingsCallSettings import SettingsCallSettings
from SettingsPhoneSettings import SettingsPhoneSettings
from SettingsSecuritySettings import SettingsSecuritySettings


class Settings:

    def display(self):
        print("settings:")
        print("1. Call settings")
        print("2. Phone settings ")
        print("3. Security settings")
        print("4. restore factory setting")

        user_input = int(input())

        if user_input == 1:
            call_settings = SettingsCallSettings()
            call_settings.display()
        elif user_input == 2:
            phone_settings = SettingsPhoneSettings()
            phone_settings.display()
        elif user_input == 3:
            security_settings = SettingsSecuritySettings()
            security_settings.display()
        elif user_input == 4:
            print("restore Factory settings")
        else:
            print("Invalid option chosen")
