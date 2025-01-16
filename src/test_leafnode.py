import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html__success(self):
        test_node = LeafNode(
            "b",
            "that is very bold of you",
            {"style": "very_bold", "border": "max_boldness"},
        )
        self.assertEqual(
            test_node.to_html(),
            "<b style=very_bold border=max_boldness>that is very bold of you</b>",
        )

    def test_to_html__value_error(self):
        test_node = LeafNode("a", None, {"href": "https://yupstilltesti.ng"})
        with self.assertRaises(ValueError):
            test_node.to_html()


if __name__ == "__main__":
    unittest.main()
