import unittest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual("Hello Imre", "Hello Imre")


if __name__ == '__main__':
    unittest.main()
