import unittest
import pandas
import json
from app.modules.base_operation import learn, plotter

class TestLean(unittest.TestCase):

    def setUp(self) -> None:
        self.target = learn.Learn()
        self.answer = json.load(open('test/assertion_data/ans.json'))
        self.data = pandas.read_csv('test/assertion_data/data.csv')
        return super().setUp()

    def tearDown(self) -> None:
        del self.target
        return super().tearDown()

    def test_x_not_set(self):

        self.target.y = 3

        with self.assertRaises(ValueError):
            self.target.init_data(0.3, 54)

    def test_y_not_set(self):

        self.target.x = 3

        with self.assertRaises(ValueError):
            self.target.init_data(0.3, 54)

    def test_learn_linear_regression(self):
        
        self.target.x = self.data.iloc[:, :5]
        self.target.y = self.data['Price']

        self.target.init_data(0.3, 54)
        self.assertAlmostEqual(self.answer['score'], self.target.linear_regression()['score'], 3)