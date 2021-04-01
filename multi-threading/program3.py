'''
Sequential programming
Without timing
'''
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double : ',2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('Square : ',n*n)

numbers = [1,2,3,4,5,6]
doubles(numbers)
squares(numbers)