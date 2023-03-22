import itertools

word = input("Enter a word: ")

permutations = []
for p in itertools.permutations(word):
    print(p)
    permutation = ''.join(p)
    print(permutation)
    permutations.append(permutation)


print("All possible combinations of the word", word, "are:")
for permutation in permutations:
    print(permutation)
