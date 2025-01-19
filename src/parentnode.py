from htmlnode import HTMLNode
from leafnode import LeafNode
from functools import reduce
from utils import *


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: "ParentNode", props: dict = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError(
                "tag is missing from the ParentNode instance. Please provide a tag when creating a ParentNode."
            )

        if not self.children:
            raise ValueError(
                "children list is missing from the ParentNode instance. Please provide a children list when creating a ParentNode."
            )

        return get_formatted_html_str(self.tag, self.parent_node_to_html(self))

    def parent_node_to_html(self, node):
        if not node:
            return ""
        if isinstance(node, LeafNode):
            return node.value
        return reduce(
            lambda acc, child: f"{acc}{get_formatted_html_str(child.tag, self.parent_node_to_html(child))}",
            node.children,
            "",
        )
