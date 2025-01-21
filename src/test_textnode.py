import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode


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

    def test_text_node_to_html_node(self):
        normal_node = TextNode("Brave New Text Node", TextType.NORMAL)
        bold_node = TextNode("A very bold one at that", TextType.BOLD)
        italic_node = TextNode("And somewhat Italian", TextType.ITALIC)
        code_node = TextNode("tap tap tap", TextType.CODE)
        link_node = TextNode("Linkity clink", TextType.LINK, "https://clickity-click")
        image_node = TextNode(
            "This image describes a beautiful prairie with black and white rabbits hopping lively all around it",
            TextType.IMAGE,
            url="https://definitely-not-a-rickroll",
        )

        normal_html_node = text_node_to_html_node(normal_node)
        self.assertEqual(normal_node.text, normal_html_node.value)


if __name__ == "__main__":
    unittest.main()
