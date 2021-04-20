from progress.bar import Bar
from app.modules.baseml import BaseML

if __name__ == '__main__':

    titanic = BaseML('titanic')
    titanic.drop(['Name', 'Ticket'])
    titanic.fix('Age', help='Sex')
    titanic.auto_fix()
    titanic.get_dummy(['Sex', 'Embarked'])
    titanic.drop('Sex_female')
    titanic.plot = False
    titanic.model = 'logistic_regression'

    res = []

    with Bar('Processing', max=20) as bar:
        for i in range(1,1000):
            titanic.random_state = i
            @titanic.train
            def train(self):

                self.data_x = self.data.drop(['Survived', 'Pclass'],axis=1)
                self.data_y = self.data['Survived']

            res.append(train['score'])

            if i%49 == 0:
                bar.next()

    best = res.index(max(res))
    print('Best random state: {best}')
    
    @titanic.train
    def train(self):

        self.data_x = self.data.drop(['Survived', 'Pclass'],axis=1)
        self.data_y = self.data['Survived']

    print(train)
        