class Doubler:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def numbers(self):
        my_doubled_numbers = []
        for num in self.numbers_list:
            my_new_num = num * 2
            my_doubled_numbers.append(my_new_num)

        print(my_doubled_numbers)
