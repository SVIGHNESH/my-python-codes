'''Construct a function insert_nth_char(s, n, char) that takes a string s, an integer n >= 0, and a character char, and inserts char at index n. If n is beyond the length of s, char is appended at the end.
insert_nth_char("MANGO", 1, 'X') returns "MXANGO"
insert_nth_char("MANGO", 5, 'X') returns "MANGOX"'''
def insert_nth_char(s, n, char):
    return s[:n] + char + s[n:]

s = input("Enter the string : ")
n = int(input("Enter the position : "))
char = input("Enter the character : ")
print(insert_nth_char(s, n, char))

