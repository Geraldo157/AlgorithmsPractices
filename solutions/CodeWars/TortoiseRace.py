def race(v1, v2, g):
    if v2 > v1:
        rel = (v2 - v1)
        h = g // rel
        min = round((((g / rel) - h) * 60) - 0.5)
        sec = round((((((g / rel) - h) * 60) - min) * 60) - 0.45)
        if sec == 60:
            return [h, min + 1, sec - 60]
        else:
            return [h, min, sec]
    else:
        return None
