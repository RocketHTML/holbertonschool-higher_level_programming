#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

if __name__ == '__main__':
    u = update_dictionary
    p = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = u(a_dictionary, 'language', "Python")
    p(new_dict)
    print("--")
    p(a_dictionary)

    print("--")
    print("--")

    new_dict = u(a_dictionary, 'city', "San Francisco")
    p(new_dict)
    print("--")
    p(a_dictionary)
