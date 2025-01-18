from htmlnode import HTMLNode
from functools import reduce
from utils import props_to_str


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError(
                "A LeafNode created with no value. All leaf nodes must have a value."
            )

        if self.tag is None:
            return str(value)

        return f"<{self.tag}{props_to_str(self.props)}>{self.value}</{self.tag}>"
