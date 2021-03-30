from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from matplotlib import pyplot

class Learn:

    _x = None
    _y = None

    _x_train = None
    _x_test  = None
    _y_train = None
    _x_test  = None

    # Constructor
    def __init__(self):
        pass

    # Getters
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # Setters
    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    # Init train data
    def init_data(self, test_size=0.3, random_state=54):

        # Make sure x and y is set
        assert(not self._x.empty)
        assert(not self._y.empty)

        self._x_train, self._x_test, self._y_train, self._y_test = train_test_split(self._x,self._y,test_size=test_size,random_state=random_state)

    # Train with linaer regression
    def linear_regression_train(self, plot=False):

        # Train and get predictions
        reg = LinearRegression()
        reg.fit(self._x_train, self._y_train)
        predictions = reg.predict(self._x_test)

        # Plot result graph if needed
        if plot:
            pyplot.scatter(self._y_test, predictions, color='blue')
            pyplot.show()

        # Return results
        return {
            "predictions" : predictions,
            "score": r2_score(self._y_test, predictions),
        }