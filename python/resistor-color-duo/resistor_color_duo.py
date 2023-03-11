def value(colors):
    res = ''
    band_colors = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
    for color in colors[:2]:
        index = str(band_colors.index(color))
        res += index
    return int(res)

print(value(["blue", "grey"]))