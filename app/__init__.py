import os
import pandas

BASEDIR = os.path.dirname(os.path.realpath(__file__))

# Housing data
housing_data = pandas.read_csv(f'{BASEDIR}/data/Housing_Dataset_Sample.csv')

from app.modules.housing import Housing
housing = Housing()

