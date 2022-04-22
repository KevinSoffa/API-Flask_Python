from models.instrumento_model import InstrumentoModel
from ma import ma


class InstrumentoSchemas(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InstrumentoModel
        load_instance = True
