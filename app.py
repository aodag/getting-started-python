import os
from pyramid.config import Configurator


def index(request):
    return "Hello, world!"


def cities(request):
    data = ['Amsterdam', 'San Francisco', 'Berlin', 'New York']
    return data


def make_app(global_conf, **settings):
    config = Configurator(settings=settings)
    config.add_route("top", "/")
    config.add_route("cities", "/cities.json")
    config.add_view(index, route_name="top", renderer="string")
    config.add_view(cities, route_name="cities", renderer="json")
    return config.make_wsgi_app()


if __name__ == '__main__':
    import waitress
    app = make_app({})
    port = int(os.environ.get('PORT', 5000))
    waitress.serve(app, port=port, host="0.0.0.0")
