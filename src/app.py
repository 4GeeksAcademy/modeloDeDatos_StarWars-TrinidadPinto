import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db

app = Flask(__name__)
app.url_map.strict_slashes = False
target_metadata = db.metadata

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/usuario', methods=['GET'])
def handle_usuarios():

    response_body = {
        "msg": "Hello, this is your GET /usuario response "
    }

    return jsonify(response_body), 200

@app.route('/personaje', methods=['GET'])
def handle_personaje():

    response_body = {
        "msg": "Hello, this is your GET /personaje response "
    }

    return jsonify(response_body), 200

@app.route('/planeta', methods=['GET'])
def handle_planeta():

    response_body = {
        "msg": "Hello, this is your GET /planeta response "
    }

    return jsonify(response_body), 200

@app.route('/vehiculo', methods=['GET'])
def handle_vehiculo():

    response_body = {
        "msg": "Hello, this is your GET /vehiculo response "
    }

    return jsonify(response_body), 200

@app.route('/favorito', methods=['GET'])
def handle_favorito():

    response_body = {
        "msg": "Hello, this is your GET /favorito response "
    }

    return jsonify(response_body), 200

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
