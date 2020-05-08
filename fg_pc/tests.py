from django.test import TestCase

# Create your tests here.
import unittest


# 写几个功能
def add(a, b):
    return a + b


def multi(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


class TestMyMath(unittest.TestCase):
    def setUp(self) -> None:
        print('开始')

    def test_sum(self):
        print('add')
        self.assertTrue(add(1, 2) == 3)

    def test_multi(self):
        print('multi')
        self.assertTrue(multi(2, 3) == 6)

    def test_sub(self):
        print('sub')
        self.assertTrue(sub(2, 3) == -1)

    def test_div_normal(self):
        print('div_normal')
        self.assertTrue(div(10, 2) == 5)

    def test_div_except(self):
        print('div_except')
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def tearDown(self) -> None:
        print('完成')


if __name__ == '__main__':
    unittest.main()
