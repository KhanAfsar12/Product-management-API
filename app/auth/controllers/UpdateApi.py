from flask import jsonify, make_response, redirect, render_template, request, url_for
from flask_restful import Resource

from app.auth.model.product import Product
from app import db

class UpdateView(Resource):

    def get(self, id):
        return make_response(render_template('update.html', id=id))

    def post(self, id):
        data = request.form

        if not data:
            return jsonify({"Message": "No data input provided"})
        
        update_obj = Product.query.filter_by(id=id).first()
        if not update_obj:
            return jsonify({"Message": "Product not found"})
        
        if 'name' in data:
            update_obj.name = data['name']
        if 'description' in data:
            update_obj.description = data['description']
        if 'price' in data:
            update_obj.price = data['price']
        if 'quantity' in data:
            update_obj.quantity = data['quantity']

        try:
            db.session.commit()
            return redirect(url_for('auth.readview'))
        except Exception as e:
            db.session.rollback()
            return jsonify({"Message": f"An error occured: {str(e)}"})