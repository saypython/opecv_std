class A:
    def __init__(self):
        self.a=None
        self._a=None
        self.__a=None
    def p(self):
        self.a=11
        self._a=12
        self.__a=13
    def g(self):
        return self.__a