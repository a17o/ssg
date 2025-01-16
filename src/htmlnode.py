from functools import reduce
from typing import List


class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: List["HTMLNode"] = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def __repr__(self):
        return HTMLNode.node_to_str(self)

    def to_html(self):
        raise NotImplementedError("whoops, nothing here yet")

    def props_to_html(self):
        return reduce(
            lambda p1, p2: p1 + " " + f'{p2[0]}="{p2[1]}"', self.props.items(), ""
        )

    def node_to_str(node: "HTMLNode", level: int = 1):
        tab = "\t"
        return f"{tab * (level - 1)}HTMLNode(\n{tab * level}tag={node.tag},\n{tab * level}value={node.value},\n{tab * level}props={node.props_to_html()}\n{tab * level}children=\n{tab * (level + 1)}{HTMLNode.children_to_str(node.children, level + 1)}\n{tab * (level - 1)})"

    def children_to_str(children: List["HTMLNode"], level: int = 1):
        if not children:
            return ""
        return reduce(
            lambda acc, c2: acc + f"\n{HTMLNode.node_to_str(c2, level)}", children, ""
        )
