
from flask_restful import Resource, reqparse
from flask import send_file

class exemple_route(Resource):
	def get(self):

		path = "./datascientest.jpg"
		return send_file(path, as_attachment=True, mimetype='image/gif')
