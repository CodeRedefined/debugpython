from flask import Flask

app = Flask(__name__)


@app.route("/")
def root_route():
    return "Flask app running!!!"


@app.route("/get_api", methods = ["GET"])
def get_method():
    return "GET API running!!!"


@app.route("/post_api", methods=["POST"])
def post_method():
    return "POST API !!!"


@app.route("/put_api", methods=["PUT"])
def put_method():
    return "PUT API !!!"


@app.route("/delete_api", methods=["DELETE"])
def delete_method():
    return "Delete API !!!"


if __name__ == "__main__":
    app.run()