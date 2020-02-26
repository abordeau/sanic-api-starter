from sanic import Blueprint, response

api_bp = Blueprint('api', url_prefix='api')


@api_bp.route('/')
async def index(request):
    return response.text('api index')
