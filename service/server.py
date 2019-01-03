import uuid

from flask import Flask, jsonify
from infrastructure.in_memory_user_repository import InMemUserRepository
from utils.log import Log

app = Flask(__name__)


log = Log().get_logger(__name__)

user_repo = InMemUserRepository()


@app.route("/login", methods=["get"])
def login():
    user_id = uuid.uuid4()
    log.info("Adding new user with user_id: %s", user_id)
    user_repo.add_user(user_id)
    return jsonify(user_id)


