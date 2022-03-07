def invert(x: dict[str, str]) -> dict[str, str]:
    y: dict[str, str] = {}
    for key in x:
        if x[key] in y:
            raise KeyError("key in dict.")
        else:
            y[x[key]] = key
    return y


def favorite_color(x: dict[str, str]) -> str:
    counter: dict[str, int] = {}
    for key in x:

        if x[key] in counter:
            counter[x[key]] += 1
        else:
            counter[x[key]] = 1
    popular: str = ""
    max: int = 0
    for color in counter:
        if counter[color] > max:
            max = counter[color]
            popular = color
    return popular


def count(x: list[str]) -> dict[str, int]:
    y: dict[str, int] = {}
    for item in x:
        if item in y:
            y[item] += 1
        else:
            y[item] = 1
    return y