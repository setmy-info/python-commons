import unittest

from arguments.argument import Argument
from arguments.config import Config
from arguments.parser import parse_arguments


class TestFoo(unittest.TestCase):
    def test_foo(self):
        argv = ["example_application_name.py", '-i', 'input.txt', '-o', 'output.txt']
        config = Config(
            'Example parser',
            [
                Argument('input', 'i', str, 'Input file', True),
                Argument('output', 'o', str, 'Output file', True)
            ])

        parsed = parse_arguments(argv, config)

        self.assertEqual(parsed.input, 'input.txt')
        self.assertEqual(parsed.output, 'output.txt')


if __name__ == '__main__':
    unittest.main()
