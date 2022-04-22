from db import db


class InstrumentoModel(db.Model):
    __tabname__ = 'instrumentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    marca = db.Column(db.String(80), nullable=False)


    def __init__(self, nome, marca ):
        self.nome = nome
        self.marca = marca

    def __repr__(self, ):
        return f'InstrumentoModel(nome={self.nome}, marca={self.marca})'

    def json(self, ):
        return{
          "nome": self.nome,
          "marca": self.marca  
        }

    @classmethod
    def find_by_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()


    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
