class AverageOfThree:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def average_calc(self):
        my_num_list = [self.num1, self.num2, self.num3]
        total = self.num1 + self.num2 + self.num3
        length_num = len(my_num_list)
        avgnum = round(total / length_num)
        print(avgnum)