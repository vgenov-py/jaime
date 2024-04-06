from flask import Flask
from views.web.routes import web
from views.api.routes import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix="/api")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5001)