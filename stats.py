def get_words(text):
    num_words = len(text.split())
    return num_words

def get_characters(text):
    chars ={}
    text = text.lower()
    for character in text:
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars

def sort_characters(characters):
    sorted_list = []
    for character in characters:
        if character.isalpha():
            sorted_list.append({"char": character, "num": characters[character]})
    
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    
    return sorted_list