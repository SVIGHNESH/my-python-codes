def filter_text(text):
    words = text.split()
    numbers=[word for word in words if word.isdigit()]

    vowels =[word for word in words if word[0] in "AEIOUaeiou"]

    nouns = [word for word in words if word in ["Agra","Ramesh","Tomato","Patna"]]

    return numbers,vowels,nouns
print(filter_text(";Ramesh us 34 year old that is liiving in the Agra for 56 years."))