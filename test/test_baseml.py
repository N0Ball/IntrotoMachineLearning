import unittest
import json
import pandas
from app.modules.baseml import BaseML
from app.modules.base_operation.plotter import Plotter

class MockBaseML(BaseML):

    def __init__(self, name):
        self.name = name
        self._data = pandas.read_csv(f'test/data/test.csv')
        self._plotter = Plotter(self.data)

class Test_BaseML(unittest.TestCase):
    
    def setUp(self) -> None:
        self.target = MockBaseML('test')
        self.answer = json.load(open('test/assertion_data/ans.json'))
        return super().setUp()

    def tearDown(self) -> None:
        del self.target
        return super().tearDown()

    def test_baseml_regression_learning(self) -> None:
        
        @self.target.train
        def train(self):

            self.data_x = self.data.iloc[:, :5]
            self.data_y = self.data['Price']

            self.plot = False

        self.assertDictEqual(train,self.answer)

if __name__ == '__main__':
    unittest.main()