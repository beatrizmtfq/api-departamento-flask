from flask import Blueprint, make_response, jsonify

from app.models.departamento import Departamento


class DepartamentoController:

    departamento = Blueprint('departamento', __name__, url_prefix='/departamentos')

    @departamento.route('/', methods=["GET"])
    def obter_todos_departamentos():

        lista_departamentos = []

        departamentos = Departamento.query.all()

        for d in departamentos:
            lista_departamentos.append(({
                "id": d.id_departamento,
                "nome": d.nome_departamento,
                "descricao": d.descricao
            }))

        resposta = make_response(jsonify(lista_departamentos))
        resposta.headers['Content-Type'] = 'application/json'

        return resposta


    @departamento.route('<int:id_departamento>', methods=["GET"])
    def obter_departamento_por_id(id_departamento):

        departamento = Departamento.query.get(id_departamento)

        if departamento:
            resposta = make_response(jsonify({
                "id": departamento.id_departamento,
                "nome": departamento.nome_departamento,
                "descricao": departamento.descricao
            }))

            resposta.headers['Content-Type'] = 'application/json'
            return resposta
        else:
            return make_response(jsonify({
                'message' : 'Departamento não encontrado'
            }), 404)


    @departamento.route('/', methods=["POST"])
    def adicionar_departamento():
        pass

    @departamento.route('/<int:id_departamento>', methods=["PUT"])
    def atualizar_departamento(id_departamento):
        pass

    @departamento.route('/<int:id_departamento>', methods=["DELETE"])
    def excluir_departamento(id_departamento):
        pass