from schemas.instrumento_schemas import InstrumentoSchemas
from models.instrumento_model import InstrumentoModel
from flask_restplus import Resource, fields
from server.instance import server
from flask import request


instrumento_ns = server.instrumento_ns
instrumento_schema = InstrumentoSchemas()
instrumento_list_schema = InstrumentoSchemas(many=True)


class InstrumentoController(Resource):
    def get(self, id):
        instrumento_data = InstrumentoModel.find_by_id(id)
        if instrumento_data:
            return instrumento_schema.dump(instrumento_data) 

