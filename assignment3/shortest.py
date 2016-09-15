def shortest(v, array):
    if v.previous:
        array.append(v.previous.getId())
        shortest(v.previous, array)
    return
