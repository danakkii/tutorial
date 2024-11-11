from flask import Flask, jsonify
# falsk 객체 생성
app = Flask(__name__)
# 라우팅 생성
@app.route('/json_text')
def hello_json():
    data = {'name':'장재원', 'location':'seoul'} # Json 형식
    return jsonify(data)
@app.route('/server_info')
def server_json():
    data = {'server_name':'0.0.0.0', 'server_port':'8080'} # Json 형식
    return jsonify(data)
# 서버 작동
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")