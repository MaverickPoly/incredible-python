def is_anagram(t1: str, t2: str):
    collection = {}
    for char in t1:
        if char in collection:
            collection[char] += 1
        else:
            collection[char] = 1

    for char in t2:
        if char not in collection or collection[char] <= 0:
            return False
        collection[char] -= 1

    return True


original_text = input("Enter the original text: ")
target_text = input("Enter the target text: ")

if is_anagram(original_text, target_text):
    print("Anagram")
else:
    print("NOT anagram")
