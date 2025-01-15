# Task 3: Count Words in a Sentence


def word_count(str):
    counts = {}
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
            # counts[word] = counts[word] + 1
        else:
            counts[word] = 1


    return counts

print(word_count("have a nice day be happy a"))