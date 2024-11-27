def sort_print( str):
    words = str.split(",")
    sorted_words = sorted(words)
    sorted_Str = ','.join(sorted_words)
    print(sorted_Str)


str = input("Enter the string:")
sort_print(str)