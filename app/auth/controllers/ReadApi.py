from flask import make_response, render_template
from flask_restful import Resource

from app.auth.model.product import Product


class ReadView(Resource):
    def get(self):
        objects = Product.query.all()
        return make_response(render_template('read.html', objects=objects))