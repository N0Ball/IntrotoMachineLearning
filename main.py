from app import housing, housing_data

if __name__ == '__main__':

    housing.plot('Price')
    housing.join_plot('Avg. Area Income', 'Price')
    housing.pair_plot()
    
    @housing.train
    def train(self):

        self.data_x = housing_data.iloc[:, :5]
        self.data_y = housing_data['Price']

    print(train)