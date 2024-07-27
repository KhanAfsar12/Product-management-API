from flask import jsonify, make_response, redirect, render_template, url_for
from flask_restful import Resource
from app import db
from app.auth.model.product import Product


class DeleteView(Resource):

    def get(self, id):
        del_obj = Product.query.filter_by(id=id).first()
        if not del_obj:
            return jsonify({"Message": "Product not found"})
        return make_response(render_template('delete.html', del_obj=del_obj))


    def post(self, id):
        delete_obj = Product.query.filter_by(id=id).first()
        if not delete_obj:
            return jsonify({"Message": "Product is not found"})
        
        db.session.delete(delete_obj)
        db.session.commit()
        return redirect(url_for('auth.readview'))