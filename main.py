
from flask import  Flask,jsonify,request
from flask_cors import CORS
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route("/api/v1/DummyApi/", methods=['GET'])
def DummyApi():
    list = [{'Name': 'Badruzzaman'}, {'Name': 'Rahim'}]
    return jsonify(list),200

@app.route("/api/v1/Create/", methods=['POST'])
def Create():
    #list = request.ar
    return jsonify(list),200

if __name__ == "__main__":
    app.run()