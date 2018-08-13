# Takes a sentence as a parameter and returns the longest word


def one_or_two():
    '''
    Determines whether the first or second value is larger
    and returns it
    '''
    word_length = len(sentence[0])
    word_length_plus_1 = len(sentence[1])

    if word_length > word_length_plus_1:
        longest_word = word_length
    else:
        longest_word = word_length_plus_1

    return longest_word


def find_longest(biggest_num):
    '''
    Takes the larger of sentence[0] or sentence[1] from one_or_two() as a parameter
    Loops through the length of the remaining sentence list and returns the LENGTH of the longest word
    '''
    for i in range(2, len(sentence)):
        if biggest_num >= len(sentence[i]):
            pass
        else:
            biggest_num = len(sentence[i])

    return biggest_num


def find_index(biggest_num):
    '''
    Takes the length of the longest word from find_longest() function and returns its index
    '''
    for i in range(len(sentence)):
        if biggest_num == len(sentence[i]):
            return i
            break


sentence = 'this is a long sentence with a bunch of random words but no punctuation and only space'

sentence = (sentence.split(" "))

largest_len = find_longest(one_or_two())

index = find_index(largest_len)

print('%s is the longest word, with a length of %s' % (sentence[index], len(sentence[index])))
