c = [
    250,
    242,
    240,
    235,
    243,
    249,
    247,
    245,
    238,
    232,
    253,
    244,
    237,
    251,
    234,
    233,
    236,
    246,
    241,
    255,
    252
]
ls = []
while len(c)>0:
    ls.append(c[0]^248)
    c = c[1:]
print(ls)