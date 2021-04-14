from app.modules.baseml import BaseML

if __name__ == '__main__':

    housing = BaseML('housing')

    housing.norm_plot('Price')
    housing.join_plot('Avg. Area Income', 'Price')
    housing.pair_plot()
    
    @housing.train
    def train(self):
        
        self.data_x = self.data.iloc[:, :5]
        self.data_y = self.data['Price']

    print(f'score: {train["score"]}')