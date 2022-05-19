
from urllib import response
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from pip import main

#object flask
app = Flask(__name__)

#object flask restful
api = Api(app)

#object flask_cors
CORS(app)
identitas = {}

#class resource
class ContohResource(Resource):
    #method get dan post
    def get(self):
        #response = {"msg":"Hallo world"}

        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data masuk"}
        return response
# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)