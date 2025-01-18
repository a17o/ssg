import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("hello there", TextType.ITALIC, "https://url.url")
        node2 = TextNode("general kenobi", TextType.BOLD, "https://url.url")
        self.assertNotEqual(node, node2)

    def test_repr__in_str(self):
        node = TextNode("hello there", TextType.ITALIC, "https://url.url")
        self.assertIn("TextNode(hello", str(node))

    def test_repr__not_in_str(self):
        node = TextNode("\{beep boop <010101>\}", TextType.CODE, "https://url.url")
        self.assertNotIn("the matrix", str(node))

    def test_textnode__has_expected_values(self):
        node = TextNode("running out of steam here", TextType.NORMAL, "https://url.url")
        self.assertIn("steam", node.text)
        self.assertEqual(TextType.NORMAL, node.text_type)
        self.assertIn("url", node.url)


if __name__ == "__main__":
    unittest.main()
