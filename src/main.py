from textnode import TextNode, TextType


def main():
    node = TextNode("cool text, dude", TextType.ITALIC, "https://urtexthere.really")
    print(node)


if __name__ == "__main__":
    main()
