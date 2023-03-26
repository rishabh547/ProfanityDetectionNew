from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
# ML model code import below 
from main import hate_speech_detection


app = Flask(__name__)
api = Api(app) # creating an API object

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Chat(Resource):
    
    def post(self):
        data = request.get_json()
        censored_text = hate_speech_detection(data)
        return {'censored': censored_text}
    

# adding the defined resources along with their corresponding urls
api.add_resource(Chat, '/chat')


# driver function
if __name__ == '__main__':

	app.run(debug = True)
