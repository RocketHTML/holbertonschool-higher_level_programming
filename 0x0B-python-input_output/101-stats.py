#!/usr/bin/python3
import sys


class Statician:
    def __init__(self):
        self.codes = [200, 401, 403, 404, 405, 500]
        self.d = {200: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        self.size = 0
        self.requests = 0

    def output(self):
        print("File size: {}".format(self.size))
        for code in self.codes:
            if self.d[code] > 0:
                print("{}: {}".format(code, self.d[code]))

    def update(self):
        line = sys.stdin.readline()
        if len(line) > 0:
            self.requests += 1
            chunks = line.split()
            try:
                code = int(chunks[-2])
                file_size = int(chunks[-1])
                if code not in self.codes:
                    self.codes.append(code)
                    self.codes.sort()
                    self.d[code] = 1
                    self.size += file_size
                else:
                    self.d[code] += 1
                    self.size += file_size
                return True
            except (IndexError, ValueError):
                return True
        else:
            return False


if __name__ == '__main__':
    stats = Statician()
    try:
        while stats.update():
            if stats.requests % 10 == 0:
                stats.output()
    except KeyboardInterrupt:
        raise
    finally:
        stats.update()
        stats.output()
