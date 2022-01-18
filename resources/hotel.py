from flask_restful import Resource, reqparse

hoteis = [
    {
        "hotel_id": "alpha",
        "nome": "alpha",
        "estrelas": 4.3,
        "diaria": 520.32,
        "cidade": "Rio de Janeiro"
    },

    {
        "hotel_id": "bravo",
        "nome": "bravo",
        "estrelas": 5,
        "diaria": 210.80,
        "cidade": "São Paulo"
    },

    {
        "hotel_id": "charlie",
        "nome": "charlie",
        "estrelas": 2.2,
        "diaria": 80.32,
        "cidade": "Brasilia"
    }

]


class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            # print(f"Esse é o 'hotel['hotel_id'] {hotel['hotel_id']} e esse o 'hotel_id' {hotel_id}")
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'hotel not foud'}, 404  # mando essa msg se nada foie ncontrado

    def post(self, hotel_id):

        # com o reqparse e o add_argumente eu pego apenas os argumentos que estou pedindo, mesmo se o usuario passar
        # algo amais eu so vou pegar aquilo que estou pedindo, nome, estrelas, diaria, cidade
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        # com isso ele cria um construtor pra mim
        dados = argumentos.parse_args()

        # e eu adiciono tudo em uma variavel, onde nessa variavel vou ter chave e valor dos argumento passados

        novo_hotel = {
            "hotel_id": hotel_id,
            "nome": dados['nome'],
            "estrelas": dados['estrelas'],
            "diaria": dados['diaria'],
            "cidade": dados['cidade']

        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
