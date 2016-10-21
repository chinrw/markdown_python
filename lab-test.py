import unittest

import markdown


class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_paragraphs(self):
        self.assertEqual(markdown.convertHead(
            '##lol##'), '<h2>lol</h2>')
        self.assertEqual(markdown.convertHead(
            '#lol#'), '<h1>lol</h1>')
        self.assertEqual(markdown.convertHead(
            '###lol###'), '<h3>lol</h3>')

    def test_blockquote(self):
        self.assertEqual(markdown.convertBlock(
            '>test'), '<blockquote>test\n</blockquote>')

if __name__ == "__main__":
    unittest.main()
