from app import app, db
from models import Usuario, Personaje, Planeta, Vehiculo, Favorito
from eralchemy2 import render_er

with app.app_context():
    db.create_all()
    render_er(db.Model.metadata, 'diagram.png')
    print("✅ Diagrama generado con éxito en diagram.png")