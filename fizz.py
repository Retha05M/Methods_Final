class FizzBuzz:
    def __init__(self, max_num):
        self.max_num = max_num

    def given_max_num_4(self):
        my_4_numbers = []
        my_max_num = self.max_num

        for number in range(1, my_max_num):
            if number % 4 == 0 and number < my_max_num:
                my_4_numbers.append(number)
        return my_4_numbers

    def given_max_num_6(self):
        my_6_numbers = []
        my_max_num = self.max_num

        for number in range(1, my_max_num):
            if number % 6 == 0 and number < my_max_num:
                my_6_numbers.append(number)
        return my_6_numbers
