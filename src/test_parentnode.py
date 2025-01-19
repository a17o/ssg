from parentnode import ParentNode
from leafnode import LeafNode
import unittest


class TestParentNode(unittest.TestCase):
    def test_to_html__nested_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "a",
                    [
                        LeafNode("s", "strikethrough text"),
                        LeafNode("div", "not how blocks work"),
                        ParentNode(
                            "b",
                            [
                                LeafNode("i", "yet another italics text"),
                                LeafNode("span", "yeah, I know"),
                            ],
                        ),
                    ],
                    {
                        "href": "https://iamnotproud.net"
                    },  # TODO: add props in the next exercise
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected_html_str = "<p><b>Bold text</b><a><s>strikethrough text</s><div>not how blocks work</div><b><i>yet another italics text</i><span>yeah, I know</span></b></a><i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html_str)

    def test_to_html__leaf_nodes_only(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected_html_str = (
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(node.to_html(), expected_html_str)

    def test_to_html__no_children(self):
        node = ParentNode(
            "b",
            [],
        )

        with self.assertRaises(ValueError):
            node.to_html()
