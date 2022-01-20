from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
    # com o reqparse e o add_argumente eu pego apenas os argumentos que estou pedindo, mesmo se o usuario passar
    # algo amais eu so vou pegar aquilo que estou pedindo, nome, estrelas, diaria, cidade
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    # como utilizei esse bloco de codigo em mais de uma parte, criei uma função

    def find_hotel(hotel_id):
        for hotel in hoteis:
            # print(f"Esse é o 'hotel['hotel_id'] {hotel['hotel_id']} e esse o 'hotel_id' {hotel_id}")
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)

        # se existiro hotel eu retorno o hotel
        if hotel:
            return hotel

        # se nao existir eu retorno o erro
        return {'message': 'hotel not foud'}, 404  # mando essa msg se nada foie ncontrado

    def post(self, hotel_id):
        # com isso ele cria um construtor pra mim
        dados = Hotel.argumentos.parse_args()

        "como era para adicionar um novo hotel"
        # # e eu adiciono tudo em uma variavel, onde nessa variavel vou ter chave e valor dos argumento passados
        #
        # novo_hotel = {
        #     "hotel_id": hotel_id,
        #     "nome": dados['nome'],
        #     "estrelas": dados['estrelas'],
        #     "diaria": dados['diaria'],
        #     "cidade": dados['cidade']
        #
        # }

        "Segundo jeito..."
        # novo_hotel = {
        #     # com o comando **dados o python desempacota todos os dados contido na variavel dados
        #     "hotel_id": hotel_id, **dados}

        "Terceiro jeito"
        hotel_objeto = HotelModel(hotel_id, **dados)
        # na função meus dados é convertido para um dicionario queé o padrão do json
        novo_hotel = hotel_objeto.json()

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        # na função meus dados é convertido para um dicionario queé o padrão do json
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201  # create /criado o hotel pois nao existiA

    def delete(self, hotel_id):
        # para referenciar a minha listad e hoteis
        global hoteis

        # eu crio uma nova lista sem o hotel que foi passado no hotel_id
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted'}, 200
