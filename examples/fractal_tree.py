import pyturtle
from random import uniform

class FractalTree(object):
    def __init__(self, init_len):
        self._turtle = pyturtle.Turtle()
        self._length = init_len

    def make_tree(self, length):
        if length > 5:
            self._turtle.forward(length)
            self._turtle.right(20)
            self.make_tree(length-uniform(0,15))
            self._turtle.left(40)
            self.make_tree(length-uniform(0,15))
            self._turtle.right(20)
            self._turtle.backward(length)

    def run(self):
        self._turtle.declinate(30)
        self._turtle.left(90)
        self._turtle.backward(100)
        self._turtle.pendown()
        self.make_tree(self._length)
        self._turtle.plot('g')


if __name__ in "__main__":
    FractalTree(75).run()
