#3.Write a python program to find the wordcount in a file for each line and then print the output.
# Finally store the output back to the file.
def word_count(str):###function initiation
    counts = dict()
    words = str.split()### using split from python library to separate words
    for word in words:### for loop starts
        if word in counts: ### word not gets repeated if present in the sentence
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count(input("enter sentences:")))#### printing output word count
