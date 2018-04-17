#!/usr/bin/python3
def multiple_returns(sentence):
    length, char = 0, None
    if len(sentence) > 0:
        length, char = len(sentence), sentence[0]
    return length, char

if __name__ == '__main__':
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
