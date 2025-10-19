dictionary = {"a": 1, "b": 2, "c": 3}

while len(dictionary) > 0:
    dictionary.popitem()
    print(dictionary)

print("The dictionary is now empty!")
