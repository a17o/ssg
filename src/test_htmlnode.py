from htmlnode import HTMLNode
import unittest


class TestHTMLNode(unittest.TestCase):
    def test_expected_fields(self):
        test_node = HTMLNode(
            "<b>",
            "this is a test (in bold)",
            [
                HTMLNode(
                    "<body>",
                    "neck",
                    [
                        HTMLNode(
                            "<a>",
                            "good value",
                            [],
                            {"href": "https://nothingtosee.here"},
                        )
                    ],
                    {"prop": 123},
                )
            ],
            {"style": "dashing", "hopes": "nonexistent"},
        )

        self.assertEqual(test_node.props["style"], "dashing")
        self.assertIn("nothing", test_node.children[0].children[0].props["href"])

    def test_repr(self):
        test_node = HTMLNode(
            "<i>",
            "this is a test (in italics)",
            [
                HTMLNode(
                    "<body>",
                    "leg",
                    [],
                    {"prop": 123},
                )
            ],
            {"sick": True, "dreams": "sometimes"},
        )

        self.assertIn("leg", str(test_node))
        self.assertIn("HTMLNode(", str(test_node))


if __name__ == "__main__":
    unittest.main()
