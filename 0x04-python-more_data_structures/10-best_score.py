#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    vals = [tuple(reversed((a, b))) for (a, b) in a_dictionary.items()]
    vals.sort()
    vals.reverse()
    return vals[0][1]

if __name__ == '__main__':
    best_score = __import__('10-best_score').best_score

    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
