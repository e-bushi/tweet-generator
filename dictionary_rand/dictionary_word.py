import random
import sys

def clean_data(number_of_words):
    word_array = []
    sentence = ""
    with open("random_words.txt") as f:
        random_words = list(f.readlines())

    number = 0

    for i in range(0, (number_of_words)):
        generate = random.randint(0, len(random_words) - 1)
        word_array.append(random_words[generate].replace("\n", ""))
        sentence += " {}".format(word_array[number])

        number += 1

    return(sentence)


if __name__ == '__main__':
    params = sys.argv[1:]
    first = int(params[0])
    print(clean_data(first))
