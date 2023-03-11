def commands(binary_str):
    handshakes = []
    indexes = []
    for i, num in enumerate(list(binary_str)):
        if num == "1":
            indexes.append(i)
    if 4 in indexes:
        handshakes.append("wink")
    if 3 in indexes:
        handshakes.append("double blink")
    if 2 in indexes:
        handshakes.append("close your eyes")
    if 1 in indexes:
        handshakes.append("jump")
    if 0 in indexes:
        handshakes.reverse()
    return handshakes
