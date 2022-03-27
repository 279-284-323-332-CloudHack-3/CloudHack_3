from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource,Api
import requests
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)


class LessThan(Resource):
    def get(self, n1, n2):
        json_result = {}
	 if int(n1) < int(n2)
       	json_result['result'] = 1 
 	 else 
		json_result['result'] = 0
        return json_result
    
    
api.add_resource(LessThan, "/<n1>/<n2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5058,
        host="0.0.0.0"
    )

