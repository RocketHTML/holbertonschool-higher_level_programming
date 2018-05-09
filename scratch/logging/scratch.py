#!/usr/bin/python3


class Log:
    def __init__(self, f):
        self.f = f
        self.post_id = 0
        self.logging = __import__("logging")
        self.time = __import__("time")
        self.logging.basicConfig(filename = '{}.log'.format(f.__name__),
            level = self.logging.DEBUG)

    def __call__(self, message):
        self.post_id += 1
        t1 = self.time.time()
        self.f(message)
        t2 = self.time.time() - t1
        t2 = t2 * 1000
        self.logging.info('id: {}\nmsg: {}\n{:.2f} miliseconds\n{:=<20}'.format(self.post_id, message, t2, ''))
        return self.post_id

@Log
def g(msg):
    print(msg)

a = g("yes")
b = g("you")
c = g("can")
print((a, b, c))
