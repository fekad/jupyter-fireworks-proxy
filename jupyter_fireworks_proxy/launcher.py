import argparse
from pathlib import Path

from fireworks import LaunchPad
from fireworks.flask_site.app import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response



def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the web server on (default: 5000)')
    parser.add_argument('--base_url', default='/', help='URL prefix (default: "/")')

    args = parser.parse_args()
    fireworks_launcher(args.port, args.base_url)



def fireworks_launcher(port, base_url):
    # https://dlukes.github.io/flask-wsgi-url-prefix.html

    base_url = ('/' + base_url.lstrip('/')).rstrip('/')
    app.wsgi_app = DispatcherMiddleware(
        Response('Not Found', status=404),
        {
            base_url: app.wsgi_app
        }
    )

    app.lp = LaunchPad.auto_load()
    app.run(host='0.0.0.0', port=port, debug=False, threaded=False)

if __name__ == '__main__':
    fireworks_launcher(port=5000, base_url='/fireworks')
