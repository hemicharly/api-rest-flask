import time
import traceback

import pandas as pd
from sklearn.externals import joblib

model_directory = '/home/hemicharly/projetos/api-rest-flask/app/main/models'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory

class PredictorService:
    model_columns = None
    clf = None

    def __init__(self):
        try:
            self.clf = joblib.load(model_file_name)
            self.model_columns = joblib.load(model_columns_file_name)
            self.train() # Start train constructor initialization application
        except Exception as e:
            print('Error constructor PredictorService: {0}'.format(str(e)))
            self.clf = None

    def predict(self, data):
        print('Started predict...')
        if self.clf:
            try:
                query = pd.get_dummies(pd.DataFrame(data))
                query = query.reindex(columns=model_columns, fill_value=0)
                prediction = list(clf.predict(query))

                result = []
                for pred in prediction:
                    result.append({'Survived': bool(pred)})

                return {'prediction': result}

            except Exception as e:
                return {'error': str(e), 'trace': traceback.format_exc()}
        else:
            return {'message': 'No model here, train first'}

    def train(self):
        print('Started train...')
        training_data = '/home/hemicharly/projetos/api-rest-flask/app/main/data/titanic.csv'
        include = ['Age', 'Sex', 'Embarked', 'Survived']
        dependent_variable = include[-1]

        from sklearn.ensemble import RandomForestClassifier as rf

        df = pd.read_csv(training_data)
        df_ = df[include]

        categoricals = []  # going to one-hot encode categorical variables

        for col, col_type in df_.dtypes.items():
            if col_type == 'O':
                categoricals.append(col)
            else:
                df_[col].fillna(0, inplace=True)  # fill NA's with 0 for ints/floats, too generic

        # get_dummies effectively creates one-hot encoded variables
        df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

        x = df_ohe[df_ohe.columns.difference([dependent_variable])]
        y = df_ohe[dependent_variable]

        # capture a list of columns that will be used for prediction
        global model_columns
        model_columns = list(x.columns)
        joblib.dump(model_columns, model_columns_file_name)

        global clf
        clf = rf()
        start = time.time()
        clf.fit(x, y)

        joblib.dump(clf, model_file_name)

        message1 = 'Trained in %.5f seconds' % (time.time() - start)
        message2 = 'Model training score: %s' % clf.score(x, y)
        return_message = 'Success. \n{0}. \n{1}.'.format(message1, message2)

        return {'message': str(return_message)}