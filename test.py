class Pizza():

    sauces = []
    _x = 1

    def __init__(self):
        pass

    def learn(self, func):
        func(self)
        return 3

    def test_x(self):
        print(self._x)

if __name__ == '__main__':
    pizza = Pizza()

    pizza.test_x()

    @pizza.learn
    def ouo(self):
        self._x = 10

    print(ouo)

    pizza.test_x()