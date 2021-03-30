import seaborn
from matplotlib import pyplot

class Plotter:

    def __init__(self, data):
        self.data = data

    def plot(self, name):
        seaborn.displot(self.data[name])
        pyplot.show()

    def join_plot(self, first, second):
        seaborn.jointplot(self.data[first], self.data[second])
        pyplot.show()

    def pair_plot(self):
        seaborn.pairplot(self.data)
        pyplot.show()

