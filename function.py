"""
    Function lesson
"""

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False


def hello(name='Ada', age='15'):
    print('Hello,', name)
    print('You are {} years old'.format(age))


hello(name='Baiboon', age=17)

number = 21
print('is {} an even? {}'.format(number, is_even(number)))