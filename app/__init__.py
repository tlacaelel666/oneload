from flask import Flask
from app import routes
import app

def create_app():
    app = Flask(__name__)
    with app.app_context():
        from . import routes

        app.register_blueprint(routes.bp)
    return app

def run():
   while run.debug : create_app()
    
   app.routes.bp.convert_url_to_mp3(tuple[object:"audio/mp3"])