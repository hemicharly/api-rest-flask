from flask_restplus import Namespace, fields

class PredictorDto:
    api = Namespace('Predictor', description='Predictor related operations')
    predictor = api.model('predictor', {
        'Age': fields.Integer(required=True, description='Age people'),
        'Sex': fields.String(required=True, description='Sexo people'),
        'Embarked': fields.String(required=True, description='Where the passenger got on the ship (C - Cherbourg, S - Southampton, Q = Queenstown)')
    })
    listPredictor = [predictor]