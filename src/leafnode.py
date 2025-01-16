from htmlnode import HTMLNode
from functools import reduce


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("A LeafNode created with no value. All leaf nodes must have a value.")

        if self.tag is None:
            return str(value)
        
        props_str = reduce(lambda acc, prop: acc + " " + f'{prop[0]}={prop[1]}', self.props.items(), "")
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

