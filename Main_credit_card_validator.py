# from Assignments import CreditCardValidator
# from PersonalPractice.Calculator import Calculator
from CreditCardValidator import CreditCardValidator


def main():
    print("Hello,Kindly Enter Card details to verify: ")
    verify = input()
    validator = CreditCardValidator()
    validator.processed_card_detail(verify)

if __name__ == "__main__":
    main()
