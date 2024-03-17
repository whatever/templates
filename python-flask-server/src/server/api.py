import flask


def blueprint():
    """Register basic api routes"""

    blueprint = flask.Blueprint("api", __name__)

    @blueprint.route("/api/1/")
    def index():
        return {"status":" ok"}, 200

    return blueprint
