from schemas.instrumento_schemas import InstrumentoSchemas
from models.instrumento_model import InstrumentoModel
from flask_restplus import Resource, fields
from server.instance import server
from flask import request


instrumento_ns = server.instrumento_ns
instrumento_schema = InstrumentoSchemas()
instrumento_list_schema = InstrumentoSchemas(many=True)


ITEM_NOT_FOUND = 'Instrumento not found'

item = instrumento_ns.model('Instrumentos', {
     'nome': fields.String(description= 'Nome instrumento'),
     'marca': fields.String(description= 'Marca instrumento')   
    })


class InstrumentoController(Resource):
    def get(self, id):
        instrumento_data = InstrumentoModel.find_by_id(id)
        if instrumento_data:
            return instrumento_schema.dump(instrumento_data), 200
        return {"message": ITEM_NOT_FOUND}, 404

    
    @instrumento_ns.expect(item)
    def put(self, id):
        instrumento_data = InstrumentoModel.find_by_id(id)
        instrumento_json = request.get_json()

        instrumento_data.marca = instrumento_json['marca']
        instrumento_data.nome = instrumento_json['nome']

        instrumento_data.save_to_db()
        return instrumento_schema.dump(instrumento_data), 200


class InstrumentoListController(Resource):
    def get(self, ):
        return instrumento_list_schema.dump(InstrumentoModel.find_all()), 200

    
    @instrumento_ns.expect(item)
    @instrumento_ns.doc('Create an Item')
    def post(self, ):
        instrumento_json = request.get_json()
        instrumento_data = instrumento_schema.load(instrumento_json)

        instrumento_data.save_to_db()

        return instrumento_schema.dump(instrumento_data), 201
