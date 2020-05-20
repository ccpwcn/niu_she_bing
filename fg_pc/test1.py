numbers = [1, 2, 3]
print('函数：')
def p(n):
    print(n)
for number in numbers:
    p(number)


print('生成器：')
def pp(number):
    yield number


for number in numbers:
    print(pp(number))
    print(pp(number).__next__())

