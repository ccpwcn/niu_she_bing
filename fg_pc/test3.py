import random


def number_builder(count):
    i = 0
    while i < count:
        i += 1
        yield random.randint(1,10)


# 现在，再生成10个随机数
numbers = number_builder(10)
print('number_builder done')
for n in numbers:
    print(n)


