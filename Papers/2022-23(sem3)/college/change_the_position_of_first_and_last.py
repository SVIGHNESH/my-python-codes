def change_str(s):
    return s[-1:] + s[1:-1] + s[:1]

str = "Hello"
changed_str = change_str(str)
print(changed_str)