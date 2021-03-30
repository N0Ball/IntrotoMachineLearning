from app import housing_data
from app.modules.base_operation.plotter import Plotter
from app.modules.base_operation.learn import Learn

class Housing:

    _plotter = Plotter(housing_data)
    _learn = Learn()

    _test_size = 0.3
    _random_state = 54

    def __init__(self):
        pass

    # Getter
    @property
    def test_size(self):
        return self._test_size

    @property
    def random_state(self):
        return self._random_state

    @property
    def data_x(self):
        return self._learn.x

    @property
    def data_y(self):
        return self._learn.y

    # Setter
    @test_size.setter
    def test_size(self, new_test_size):
        self._test_size = new_test_size

    @random_state.setter
    def random_state(self, new_random_state):
        self._random_state = new_random_state

    @data_x.setter
    def data_x(self, new_x):
        self._learn.x = new_x

    @data_y.setter
    def data_y(self, new_y):
        self._learn.y = new_y

    # Drawing methods
    def plot(self, name):
        self._plotter.plot(name)

    def join_plot(self, first, second):
        self._plotter.join_plot(first, second)

    def pair_plot(self):
        self._plotter.pair_plot()

    # Learning methods
    def train(self, func):

        func(self)
        
        self._learn.init_data(self._test_size, self._random_state)
        return self._learn.linear_regression_train(True)