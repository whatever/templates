import unittest


from server.app import get_app


class TestFlaskServer(unittest.TestCase):
    def test_can_init(self):
        """Test whether we can initialize the flask app and hit some pre-defined routes"""

        app = get_app()

        with app.test_client() as c:
            response = c.get("/api/1/")
            self.assertEqual(response.status_code, 200)
