#Construct a function replace_nth_char(s, n, char) that takes a string s, an integer n >= 0, and a character char, and replaces the character at index n with char. If n is beyond the length of s, the entire string is returned.
def replace_nth_char(s, n, char):
    if n < len(s):
        return s[:n] + char + s[n+1:]
    else:
        return s
    #Test the function
s  = "Hello, World!"
n = 