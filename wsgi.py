import os

from app import create_app

app = create_app()

env = os.getenv('ENV', 'DEV')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2001, debug=True, auto_reload=True, workers=2)
