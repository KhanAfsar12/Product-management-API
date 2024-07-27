from flask import Blueprint
from flask_restful import Api
from app.auth.controllers.CreateApi import CreateView
from app.auth.controllers.ReadApi import ReadView
from app.auth.controllers.DeleteApi import DeleteView
from app.auth.controllers.UpdateApi import UpdateView


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth", template_folder='templates' )

api = Api(auth_blueprint)

api.add_resource(CreateView, '/create/')
api.add_resource(ReadView, '/read/')
api.add_resource(DeleteView, '/delete/<int:id>')
api.add_resource(UpdateView, '/update/<int:id>')