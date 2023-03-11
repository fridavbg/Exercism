def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if sorted(candidate.lower()) == sorted(word.lower()):
            if candidate.lower() != word.lower():
                anagrams.append(candidate)
    return anagrams


candidates = ["Banana"]
print(find_anagrams("BANANA", candidates))