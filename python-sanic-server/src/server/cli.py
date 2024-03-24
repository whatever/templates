#!/usr/bin/env python3

import argparse

import random

from sanic import Sanic
from sanic.worker.loader import AppLoader
from .app import get_app

from x_x import splash


def parameterized_app():
    return get_app(random.randint(0, 666_666))


def main():
    parser = argparse.ArgumentParser(description='Run the Sanic app')
    parser.add_argument("--host", type=str)
    parser.add_argument("--port", type=int)
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--message", type=str)
    args = parser.parse_args()

    print(splash("tails"))

    loader = AppLoader(factory=parameterized_app)

    app = loader.load()

    app.prepare(
        host=args.host,
        port=args.port,
        workers=args.workers,
        dev=True,
    )

    Sanic.serve(primary=app, app_loader=loader)
