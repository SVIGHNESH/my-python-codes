def count_letter(sequence):
    upper = sum(1 for x in sequence if x.isupper())
    lower = sum(1 for x in sequence if x.islower())

    print(f"Upper Letter:{upper}")
    print(f"Lowercase Letters:{lower}")
sequence = input("Enter the comma separated sequence:")
count_letter(sequence)
