def wave(people):
    wave = []
    for i, v in enumerate(people):
        if v == " ":
            pass
        else:
            person = list(people)
            person[i] = v.upper()
            name = ''
            for x in person:
                name += x
            wave.append(name)
    return wave
