import unittest
from foo_bar_lib_probe.foo import foo


class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo("Imre"), "Hello Imre")


if __name__ == '__main__':
    unittest.main()
