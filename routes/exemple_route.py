
from flask_restful import Resource, reqparse
from flask import send_file

class exemple_route(Resource):
	def get(self):

		return send_file("./datascientest.jpg", as_attachment=True, mimetype='image/gif')
