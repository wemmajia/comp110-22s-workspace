def repeat(a:str,b:int) -> str:
    i = 0
    j = b
    result: str = ""
    while len(result) < len(a)*b:
        while b > 0:
            result += a[i]
            b -= 1
        b = j
        i += 1
    return result
