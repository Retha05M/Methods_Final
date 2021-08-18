from palindrome import Palindrome
from dble import Doubler
from fizz import FizzBuzz
from avg import AverageOfThree
from good import GoodBye

palin=Palindrome('sad')
print(palin.reversed_word())

double= Doubler( [1,2,3,4,5,6])
double.numbers()

fizz= FizzBuzz(20)
print(fizz.given_max_num_6())

avg_of_3= AverageOfThree(5,5,5)
avg_of_3.average_calc()

good_obj= GoodBye('Rethabile')
print(good_obj.goodbye_to())






