numbers = [1, 2, 3]


def pp(number):
    yield number


for number in numbers:
    print(pp(number))
    print(pp(number).__next__())

