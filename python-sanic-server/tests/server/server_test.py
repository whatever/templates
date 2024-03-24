import pytest
from sanic import request, response
import unittest

from server.app import get_app
from sanic_testing.testing import SanicTestClient


# XXX: Is this necessay?
@pytest.fixture
def app():
    return get_app(0)


class TestServer(unittest.TestCase):
    def test_server(self):
        app = get_app(0)
        client = SanicTestClient(app)
        request, response = app.test_client.get("/static/index.html")
        self.assertEqual(200, response.status)
