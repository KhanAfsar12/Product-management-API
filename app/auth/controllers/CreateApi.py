from flask import jsonify, make_response, redirect, render_template, request, url_for
from flask_restful import Resource

from app.auth.model.product import Product
from app import db

class CreateView(Resource):

    def get(self):
        return make_response(render_template('create.html'))
    
    def post(self):
        data = request.form
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        quantity = data.get('quantity')

        if not(name and description and price and quantity):
            return jsonify({"Message": "Please enter all fields"})

        
        new_product = Product(name=name, description=description, price=price, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('auth.readview'))    

    