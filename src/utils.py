from functools import reduce

def props_to_str(props):
    return reduce(
        lambda acc, prop: acc + " " + f"{prop[0]}={prop[1]}", props.items(), ""
    )
