def longest_unique_substring(s):
    max_length = 0
    for i in range(len(s)):
        seen = []
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.append(s[j])
        max_length = max(max_length, len(seen))
    return max_length


s = input("Enter a string: ")
print("Length of the longest unique substring:", longest_unique_substring(s))
