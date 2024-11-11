from flask import Flask, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

# endpoint, 경로지정위치 설정, app.route('/predict',method=['POST'])

@app.route('/')
class HelloWorld(Resource):
    def hello():
        return 'Hello, My First Flask!'

@app.route('/predict',methods=['POST']) # 엔드 포인트 경로(=/predict), 이미지 파일은 http post 요청을 통해서 보내지기에 , post 요청에만 허용
# def predict():
#     return 'Hello World'


def predict():
    return jsonify({'class_id':'IMAGE_NET_XXX', 'class_name':'Cat'}) 


if __name__ == '__main__':
    app.run()
    