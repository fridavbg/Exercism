def transform(legacy_data):
    new_data = {}
    for score in legacy_data:
        for letter in legacy_data[score]:
            new_data[letter.lower()] = score
    return new_data

