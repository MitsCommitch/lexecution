from flask import Flask, jsonify, request, g, Response
from flask_cors import CORS
from http import HTTPStatus
import json
import os


def create_app(game):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    @app.route('/')
    def root():
        return Response("KingArgaroth's Lexecution", status=HTTPStatus.OK)

    @app.route("/status")
    def status():
        try:
            stats = json.dumps(game.status())
        except Exception as e:
            return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return Response(stats, status=HTTPStatus.OK)
    
    @app.route("/word")
    def word():
        try:
            word = game.status().get('curr')
        except Exception as e:
            return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

        if word:
            return Response(word, status=HTTPStatus.OK)
    
    @app.route("/new")
    def new_game():
        try:
            game.new_game()
        except Exception as e:
            return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return Response(status=HTTPStatus.OK)
    
    @app.route("/guess", methods=["POST"])
    def guess():
        guess = request.get_data()
        if not guess:
            return Response(status=HTTPStatus.BAD_REQUEST)
        else:
            guess = guess.decode()
            message = game.guess(guess)
            return Response(response=message, status=HTTPStatus.OK)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()