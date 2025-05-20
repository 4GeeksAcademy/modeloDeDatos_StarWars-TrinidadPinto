from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
import enum

db = SQLAlchemy()

class TipoFavoritoEnum(enum.Enum):
    Personaje = "personaje"
    Planeta = "planeta"
    Vehiculo = "vehiculo"

class Usuario(db.Model):
    __tablename__ = 'usuarios'    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String())
    apellido = db.Column(db.String())
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True, cascade="all, delete")
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
        }

class Personaje(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    genero = db.Column(db.String())
    altura = db.Column(db.String())
    peso = db.Column(db.String())
    color_pelo = db.Column(db.String())
    color_ojos = db.Column(db.String())
    nacimiento = db.Column(db.String())
    favoritos = db.relationship('Favorito', backref='personaje', lazy=True, cascade="all, delete")
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "altura": self.altura,
            "peso": self.peso,
            "color_pelo": self.color_pelo,
            "color_ojos": self.color_ojos,
            "nacimiento": self.nacimiento,
        }

class Planeta(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    clima = db.Column(db.String())
    terreno = db.Column(db.String())
    diametro = db.Column(db.String())
    poblacion = db.Column(db.String())
    favoritos = db.relationship('Favorito', backref='planeta', lazy=True, cascade="all, delete")
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "terreno": self.terreno,
            "diametro": self.diametro,
            "poblacion": self.poblacion,
        }

class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String())
    max_velocidad = db.Column(db.String())
    tipo = db.Column(db.String())
    capacidad = db.Column(db.String())
    favoritos = db.relationship('Favorito', backref='vehiculo', lazy=True, cascade="all, delete")
    def to_dict(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "max_velocidad": self.max_velocidad,
            "tipo": self.tipo,
            "capacidad": self.capacidad
        }
    
class Favorito(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tipo = db.Column(Enum(TipoFavoritoEnum), nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('personajes.id'), nullable=True)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planetas.id'), nullable=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=True)
    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "tipo": self.tipo,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id,
            "vehiculo_id": self.vehiculo_id
        }