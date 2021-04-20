import pandas

from app import BASEDIR
from app.modules.base_operation.plotter import Plotter
from app.modules.base_operation.learn import Learn

class BaseML:

    _learn = Learn()

    _test_size = 0.3
    _random_state = 54
    _plot = True
    _model = 'linear_regression'

    # Constructors
    def __init__(self, name):
        self.name = name
        self._data = pandas.read_csv(f'{BASEDIR}/data/{name}.csv')

        self._plotter = Plotter(self.data)

    # Getter
    @property
    def test_size(self) -> int:
        return self._test_size

    @property
    def random_state(self) -> int:
        return self._random_state

    @property
    def data_x(self):
        return self._learn.x

    @property
    def data_y(self):
        return self._learn.y

    @property
    def data(self):
        return self._data

    @property
    def model(self) -> str:
        return self._model

    @property
    def plot(self) -> bool:
        return self._plot

    # Setter
    @test_size.setter
    def test_size(self, new_test_size: int) -> None:
        self._test_size = new_test_size

    @random_state.setter
    def random_state(self, new_random_state: int) -> None:
        self._random_state = new_random_state

    @data_x.setter
    def data_x(self, new_x) -> None:
        self._learn.x = new_x

    @data_y.setter
    def data_y(self, new_y) -> None:
        self._learn.y = new_y

    @model.setter
    def model(self, new_model: str) -> None:
        self._model = new_model

    @plot.setter
    def plot(self, new_plot: bool) -> None:
        self._plot = new_plot

    # Drawing methods
    def norm_plot(self, name):
        self._plotter.plot(name, title=f'{self.name}\'s Normal {name} Graph')

    def join_plot(self, first, second):
        self._plotter.join_plot(first, second, title=f'{self.name}\'s Join {first}, {second} Graph')

    def pair_plot(self, data=None):
        if data:
            self._plotter.pair_plot(data, title=f'{self.name}\'s Pair Graph ')
        else:
            self._plotter.pair_plot(title=f'{self.name}\'s Pair Graph ')

    # Data methods
    def drop(self, fields):
        self._data.drop(fields, axis=1, inplace=True)

    def info(self):
        print(self._data.info())

    def get_dummy(self, columns):
        self._data = pandas.get_dummies(data=self._data, columns=columns)

    def fix(self, data, help=None):

        if help is not None:

            self._data[data] = self._data.groupby(help)[data].apply(lambda x: x.fillna(x.median()))

        else:

            if repr(self._data.dtypes[data]) == "dtype('float64')" or repr(self._data.dtypes[data]) == "dtype('int64')":
                self._data[data].fillna(self.data[data].median(), inplace=True)

            if repr(self._data.dtypes[data]) == "dtype('O')":
                self._data[data].fillna(self._data[data].value_counts().idxmax(), inplace=True)

    def auto_fix(self):
        
        for data in self._data:
            
            if self._data[data].isnull().sum() > ( len(self._data[data])/2 ):
                print(f'Dropped {data}!')
                self.drop(data)
                continue

            if self._data[data].isnull().sum() > 0:

                self.fix(data)

    # Learning methods
    def train(self, func):

        func(self)
        
        self._learn.init_data(self.test_size, self.random_state)

        try:
            return getattr(self._learn, self.model)(self.plot)
        except Exception as e:
            print(f'Wrong model name')
            print(e)
            exit()