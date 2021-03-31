import seaborn
from matplotlib import pyplot

def draw(func):

    def aux(*args, **kwargs):

        func(*args, **kwargs)

        try:
            pyplot.title(kwargs['title'])
        except:
            pyplot.title('Default Title')

        pyplot.show()
        return func

    return aux

class Plotter:

    def __init__(self, data):
        self.data = data

    @draw
    def plot(self, name, title='Default', a = 3):
        seaborn.displot(self.data[name])

    @draw
    def join_plot(self, first, second, title='Default'):
        seaborn.jointplot(x=self.data[first], y=self.data[second])

    @draw
    def pair_plot(self, title='Default'):
        seaborn.pairplot(self.data)

