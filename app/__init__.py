from sanic import response, Sanic

from .api import api_bp
from .config import Config


def create_app() -> Sanic:
    app = Sanic(__name__)
    app.config.from_object(Config)

    @app.route("/")
    async def index(request):
        return response.text('sanic-api is running')

    @app.route('/favicon.ico')
    async def favicon(request):
        return response.redirect(
            'http://download.seaicons.com/download/i103367/paomedia/small-n-flat/paomedia-small-n-flat-cat.ico')

    app.blueprint(api_bp)

    return app
