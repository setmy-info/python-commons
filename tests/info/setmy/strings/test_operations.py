import unittest

from info.setmy.strings.operations import find_named_placeholders, replace_named_placeholder, combined_list


class TestFoo(unittest.TestCase):
    def test_find_named_placeholders(self):
        placeholders_text = "abc ${def} ghi ${jkl} mno ${prs}"
        result = find_named_placeholders(placeholders_text)
        self.assertEqual(result, ['def', 'jkl', 'prs'])

    def test_find_named_placeholders_no_default(self):
        placeholders_text = "abc ${def} ghi ${jkl} mno ${prs}"
        result = find_named_placeholders(placeholders_text, False)
        self.assertEqual(result, ['${def}', '${jkl}', '${prs}'])

    def test_replace_named_placeholder(self):
        placeholders_text = "abc ${def} ghi ${jkl} mno ${prs}"
        result = replace_named_placeholder(placeholders_text, "jkl", "Hello World")
        self.assertEqual(result, "abc ${def} ghi Hello World mno ${prs}")
        result = replace_named_placeholder(result, "prs", "qwerty")
        self.assertEqual(result, "abc ${def} ghi Hello World mno qwerty")
        result = replace_named_placeholder(result, "def", "asdf")
        self.assertEqual(result, "abc asdf ghi Hello World mno qwerty")
        # Does not replace without placeholder markers
        result = replace_named_placeholder(result, "asdf", "ghjkl")
        self.assertEqual(result, "abc asdf ghi Hello World mno qwerty")

    def test_find_named_placeholders_no_default(self):
        list1 = ["A", "B", "C"]
        list2 = ["X", "Y"]
        result = combined_list(list1, list2)
        self.assertEqual(result, ['AX', 'AY', 'BX', 'BY', 'CX', 'CY'])


if __name__ == '__main__':
    unittest.main()
