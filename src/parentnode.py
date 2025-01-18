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
                "children list is missing from ParentNode instance. Please provide a children list when creating a ParentNode."
            )
