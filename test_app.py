import pytest


@pytest.fixture
def app():
    import webtest
    from app import make_app
    app = make_app({})
    return webtest.TestApp(app)


def test_index(app):
    response = app.get('/cities.json')
    assert response.status_int == 200
    assert response.json == ['Amsterdam', 'San Francisco', 'Berlin', 'New York']
