import argparse

from getpass import getpass
from .app import get_app
from .wsgi import KnockKnockApp
from werkzeug.security import generate_password_hash

from x_x import splash


def main():

    parser = argparse.ArgumentParser(description="knock*knock")
    parser.add_argument("--host", default="0.0.0.0", help="host address")
    parser.add_argument("--port", default=8181, help="port number")
    parser.add_argument("--workers", default=2, help="number of workers")
    parser.add_argument("--bootstrap", action="store_true", help="bootstrap the database")
    args = parser.parse_args()

    print(f"\033[92m{splash('frog')}\033[0m", end="\n\n")

    options = {
        "bind": f"{args.host}:{args.port}",
        "workers": args.workers,
    }

    app = get_app()

    KnockKnockApp(app, options).run()


# def register():
#     """Register an email with a password"""
#
#     parser = argparse.ArgumentParser(description="register user/password")
#     parser.add_argument("email", type=str, help="email address")
#     args = parser.parse_args()
#
#     email = args.email
#     hashword = generate_password_hash(
#         getpass("enter password:"),
#         # method="sha256",
#     )
#
#     user = AdminUser(
#         email=email,
#         password=hashword,
#     )
#
#     app = get_app(None, False)
#
#     with app.app_context():
#         try:
#             auth_db.session.add(user)
#             auth_db.session.commit()
#         except Exception as e:
#             print("Failed with error:", e)
