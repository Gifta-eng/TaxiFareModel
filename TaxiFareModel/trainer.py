# imports
from os import pipe
from TaxiFareModel.data import clean_data, get_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd

class Trainer():
    def __init__(self, X, y):
        """
            X: pandas series
            y: pandas series
        """
        df = get_data()
        clean_data(df)        
        self.X = df.drop(columns=['fare_amount'])
        self.y = df['fare_amount']
        
        #holdout
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3)


    def set_pipeline(self):
        """defines the pipeline as a class attribute"""
        pipe = Pipeline(steps=[('scaler', StandardScaler()),
                           ('regressor', LinearRegression())])
        return pipe

    def run(self):
        """set and train the pipeline"""
        pipe = Pipeline(steps=[('scaler', StandardScaler()),
                           ('regressor', LinearRegression())])
        pipe.fit(self.X_train, self.y_train)
        pipe.transform(self.X_test, self.y_test)
        

    def evaluate(self, X_test, y_test):
        """evaluates the pipeline on df_test and return the RMSE"""
        piper = self.run
        piper.score(self.X_test, self.y_test)


if __name__ == "__main__":
    # get data
    # clean data
    # set X and y
    # hold out
    # train
    # evaluate
    print('TODO')

