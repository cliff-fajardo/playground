word1 = "ab"
word2 = "pqrs"
# output "apbqrs"

def merge_string(w1, w2):
    merged = ""
    i = 0
    len_w1 = len(w1)
    len_w2 = len(w2)
    len_merged = len(w1+w2)

    combined = w1 + w2

    while i < len_merged:
        if i < len_w1:
            merged += w1[i]

        if i < len_w2:
            merged += w2[i]

        i += 1
    return merged

word = merge_string(word1, word2)

print(word)


