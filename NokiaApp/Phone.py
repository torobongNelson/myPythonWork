from array_snacks import ArraySnacks
from nokia_app import Nokia


def main():
    #     nokia_phone = Nokia()
    #     nokia_phone.display()
    #
    #
    # if __name__ == "__main__":
    #     main()

    arr = [1, 2, 3, 4, 5]
    snacks = ArraySnacks(arr)
    print(snacks.largest_number_in_array())
    snacks.reverse_array()
