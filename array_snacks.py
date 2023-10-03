class ArraySnacks:
    def __init__(self, arr):
        self.arr = arr

    def largest_number_in_array(self):
        max_num = self.arr[0]
        for num in self.arr:
            if num > max_num:
                max_num = num
        return max_num

    def reverse_array(self):
        for index in range(len(self.arr) - 1, -1, -1):
            print(self.arr[index], end=' ')

          def does_number_exist_in_array(numbers, number):
                for i in numbers:
                    if i == number:
                        return True
                return False

        def print_elements_on_odd_positions_in_array(numbers):
            for i in range(1, len(numbers), 2):
                print(numbers[i], end=' ')

        def print_elements_on_even_positions_in_array(numbers):
            for i in range(0, len(numbers), 2):
                print(numbers[i], end=' ')

        def compute_the_running_total_in_array(numbers):
            total = 0
            for num in numbers:
                total += num
            return total

        def is_palindrome(string):
            return string == string[::-1]

        def compute_the_sum_with_while_loop(numbers):
            total = 0
            i = 0
            while i < len(numbers):
                total += numbers[i]
                i += 1
            return total

        def compute_the_sum_with_do_while_loop(numbers):
            total = 0
            i = 0
            while i < len(numbers):
                total += numbers[i]
                i += 1
            return total


# Example usage:
