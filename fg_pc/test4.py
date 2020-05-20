def have(n):
    print('before')
    yield n > 0
    print('after')


h = have(1)
print(h)
print(h.__next__())
print('外部调用结束')
print(h.__next__())

