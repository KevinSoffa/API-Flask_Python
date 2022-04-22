from controller.instrumento_controller import InstrumentoController
from marshmallow import ValidationError
from server.instance import server
from flask import jsonify
from ma import ma
from db import db


api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(InstrumentoController, '/instrumentos/<int:id>')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()