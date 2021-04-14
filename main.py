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

    for i in range(1,100):
        titanic.random_state = i
        @titanic.train
        def train(self):

            self.data_x = self.data.drop(['Survived', 'Pclass'],axis=1)
            self.data_y = self.data['Survived']

        res.append(train['score'])

    print(res.index(max(res)))
        