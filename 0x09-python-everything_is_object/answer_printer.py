#!/usr/bin/python3

"""This module creates new files with indexed names

    The main program is a loop which takes in user input
    but it can also be run from the commandline.

    Format is:
        1-answer.txt
        <index>-<filename>.<ext>
    Usage from commandline:
        $ ./answer_printer.py 0 yes no yes

         ./answer_printer.py <start index> answer_0 ans_1 ans_2 [... ans_n]

    Usage from interactive mode:
        $ answer_printer
        > command [input]

    Commands for interactive mode:
        skip
        back
        index
        filename
        extension
        w
        r
"""

class AnswerPrinter:
    def __init__(self):
        self.index = 0
        self.filename = "answer"
        self.ext = "txt"

    def command_line(self, argv):
        if len(argv) < 3:
            raise ValueError("Usage: \n./answer_printer.py idx [answers]")
        self.index = int(argv[1])
        args = argv[2:]
        for i in range(self.index, self.index + len(args)):
            filename = str(i) + '-' + self.filename + '.' + self.ext
            with open(filename, "w") as f:
                print(args[i - self.index], file=f)

    def skip(self):
        self.index += 1

    def back(self):
        self.index -= 1

    def ext(self):
        pass

if __name__ == '__main__':
    from sys import argv
    ap = AnswerPrinter()
    ap.command_line(argv)
