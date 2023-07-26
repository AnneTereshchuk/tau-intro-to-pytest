class Accumulator:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more

    @count.setter
    def count(self, value):
        raise AttributeError("can't set attribute 'count'")
    """dodala bo ne shlo """
