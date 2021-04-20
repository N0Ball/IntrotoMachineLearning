import pandas
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score

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
    def init_data(self, test_size, random_state):

        # Make sure x and y is set
        if self._x is None:
            raise ValueError('x must be set')
        if self._y is None:
            raise ValueError('y must be set')

        self._x_train, self._x_test, self._y_train, self._y_test = train_test_split(self._x,self._y,test_size=test_size,random_state=random_state)

    # Train with linaer regression
    def linear_regression(self, plot=False):

        # Train and get predictions
        reg = LinearRegression()
        reg.fit(self._x_train, self._y_train)
        predictions = reg.predict(self._x_test)

        # Plot result graph if needed
        if plot:
            pyplot.scatter(self._y_test, predictions, color='blue')
            pyplot.title('Scattered Graph')
            pyplot.show()

        # Return results
        return {
            "predictions" : list(predictions),
            "score": r2_score(self._y_test, predictions),
        }

    # Train with Logistic Regression
    def logistic_regression(self, plot=False):

        # Train and get predictions
        lr = LogisticRegression(max_iter=1000)
        lr.fit(self._x_train, self._y_train)
        predictions = lr.predict(self._x_test)

        # Plot result graph if needed
        if plot:
            pyplot.scatter(self._y_test, predictions, color='blue')
            pyplot.title('Scattered Graph')
            pyplot.show()

        # Return results
        return {
            "predictions" : list(predictions),
            "score": accuracy_score(self._y_test, predictions),
        }