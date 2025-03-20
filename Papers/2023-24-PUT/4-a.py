def remove_nth_occurrence(s, char, n):
    count = 0
    result=""
    for c in s:
        if c == char:
            count+=1
            if count ==n:
                continue
        result += c 
    return result

print(remove_nth_occurrence("banana", 'a', 1))  # Output: "bnana"
