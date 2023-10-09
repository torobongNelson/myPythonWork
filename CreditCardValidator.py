class CreditCardValidator:

    def get_card_details_length(self, card_details):
        return len(card_details)

    def is_card_digit_length_valid(self, card_details):
        if 13 <= len(card_details) <= 16:
            return True
        return False

    def get_card_type(self, card_details):
        if card_details.startswith("4"):
            return "Visa Card"
        elif card_details.startswith("5"):
            return "Master Card"
        elif card_details.startswith("6"):
            return "Discover Card"
        elif card_details.startswith("37"):
            return "American Express Card"
        return "Invalid card type"

    def is_card_details_valid(self, card_details):
        total_sum = 0
        double_digit = False

        for digit in card_details[::-1]:
            digit = int(digit)

            if double_digit:
                digit *= 2
                if digit > 9:
                    digit = digit % 10 + digit // 10

            total_sum += digit
            double_digit = not double_digit

        if total_sum % 10 == 0:
            return "Valid"
        else:
            return "Invalid"

    def processed_card_detail(self, card_details):
        check_card_detail_length = self.is_card_digit_length_valid(card_details)

        if check_card_detail_length:
            print("***************************************")
            print(f"**Credit Card Type: {self.get_card_type(card_details)}")
            print(f"**Credit Card Number: {card_details}")
            print(f"**Credit Card Digit Length: {self.get_card_details_length(card_details)}")
            print(f"**Credit Card Validity Status: {self.is_card_details_valid(card_details)}")
            print("***************************************")
        else:
            print("Please be informed, Card Detail must be between 13 and 16 in length.")


