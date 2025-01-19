from functools import reduce


def props_to_str(props):
    return reduce(
        lambda acc, prop: acc + " " + f"{prop[0]}={prop[1]}", props.items(), ""
    )


get_open_tag = lambda tag: f"<{tag}>" if tag else ""
get_close_tag = lambda tag: f"</{tag}>" if tag else ""
get_formatted_html_str = (
    lambda tag, value: f"{get_open_tag(tag)}{value}{get_close_tag(tag)}"
)
