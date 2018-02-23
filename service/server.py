import uuid
from flasgger import swag_from, Swagger
from flask import Flask, jsonify
from flask_cors import CORS

from infrastructure.in_memory_user_repository import InMemUserRepository
from utils.log import Log

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
Swagger(app, template_file='swagger/template.yml')

log = Log().get_logger(__name__)

user_repo = InMemUserRepository()


@app.route("/login", methods=["get"])
@swag_from("swagger/login.yml")
def login():
    user_id = uuid.uuid4()
    log.info("Adding new user with user_id: %s", user_id)
    user_repo.add_user(user_id)
    return jsonify(user_id)


