from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
api.add_resource(Pokemon, '/api/v1/pokemon')

pokedex = [{
    'number': 14,
    'name': 'Kakuna',
    'type': ['bug', 'poison'],
    'weaknesses': ['fire', 'flying', 'physic'],
    'evolutions': [{'number': 15, 'name': 'beedrill'}]
    }, {
    'number': 16,
    'name': 'Pidgey',
    'type': ['normal', 'flying'],
    'weaknesses': ['electric', 'ice', 'rock'],
    'evolutions': [{'number': 17, 'name': 'Pidgeotto'},
                   {'number': 18, 'name': 'Pidgeot'}]
    }, {
    'number': 50,
    'name': 'Dugtrio',
    'type': ['ground'],
    'weakness': ['grass', 'ice', 'water'],
    'evolutions':[]
    }]


class Pokemon(Resource):
    def get(self):
        """Retrieve a single Pokemon from the Pokedex. Parse arguements and give results in a dictionary"""
        parser = reqparse.RequestParser()
        parser.add_argument('number', required=False, type=int, location='args')
        args = parser.parse_args(strict=True)
        number = args.get('number')
        if number is not None:
            if number in [pokemon['number'] for pokemon in pokedex]:
                return [pokemon for pokemon in pokedex if pokemon['number'] == number][0]
            else:
                return {}
        return pokedex

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, location='json')
        parser.add_argument('number', type=int, required=True, location='json')

        args = parser.parse_args(strict=True)
        pokemon = {'name': args['name'], 'number': args['number']}

        if pokemon in pokedex:
            return {}

        pokedex.append(pokemon)
        return pokedex[-1]


if __name__ == '__main__':
    app.run(debug=True)
