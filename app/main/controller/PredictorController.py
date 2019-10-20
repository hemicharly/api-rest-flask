from flask import request, jsonify
from flask_restplus import Resource

from ..models.dto.PredictorDto import PredictorDto
from ..service.PredictorService import PredictorService

api = PredictorDto.api
predictorDto = PredictorDto.predictor
listPredictor = PredictorDto.listPredictor
sv = PredictorService()


@api.route('/')
@api.response(404, 'Predict not found')
class Predict(Resource):

    @api.expect(listPredictor, validate=True)
    @api.response(200, 'Predict successfully executed')
    @api.doc('Predict executed')
    def post(self):
        """
        Return result predict
        """
        return sv.predict(data=request.json)

@api.route('/train')
@api.response(404, 'Predict train not found')
class PredictTrain(Resource):

    @api.response(200, 'Train successfully executed')
    def get(self):
        """
        Return result train
        """
        return sv.train()