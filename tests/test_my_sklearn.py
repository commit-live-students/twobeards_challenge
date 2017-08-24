from unittest import TestCase
from build import my_sklearn
import pandas as pd, numpy as np

class TestMy_sklearn(TestCase):

    def test_load_data(self):
        titanic = my_sklearn(path="./data/titanic_train.csv", target_variable='Survived')

        self.assertEqual(titanic.target_variable, 'Survived')

        titanic.load_data(train_size=0.8)

        # Check if data is a dataframe or numpy array
        self.assertTrue(isinstance(titanic.data, np.ndarray) or isinstance(titanic.data, pd.DataFrame))

        # Checks no of rows in split
        self.assertEqual(titanic.target.shape[0], 712)

        # Checks target variable
        self.assertEqual(titanic.target_variable, 'Survived')

        # Checks feature names
        self.assertItemsEqual(titanic.feature_names, ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age',
                                                      'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
                                                      ]
                              )
