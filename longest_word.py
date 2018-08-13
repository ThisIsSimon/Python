# Takes a sentence as a parameter and returns the longest word


def one_or_two():
    word_length = len(sentence[0])
    word_length_plus_1 = len(sentence[1])

    if word_length > word_length_plus_1:
        longest_word = word_length
    else:
        longest_word = word_length_plus_1

    return longest_word


def find_longest(biggest_num):
    for i in range(2, len(sentence)):
        if biggest_num >= len(sentence[i]):
            pass
        else:
            biggest_num = len(sentence[i])

    return biggest_num


def find_index(biggest_num):
    for i in range(len(sentence)):
        if biggest_num == len(sentence[i]):
            return i


sentence = 'this is a long sentence with a bunch of random words but no punctuation and only space'

sentence = (sentence.split(" "))

largest_len = find_longest(one_or_two())

index = find_index(largest_len)

print('%s is the longest word, with a length of %s' % (sentence[index], len(sentence[index])))
