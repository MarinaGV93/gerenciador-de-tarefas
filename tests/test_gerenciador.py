from fastapi.testclient import TestClient
from fastapi import status
from gerenciador_tarefas.gerenciador import app, TAREFAS

# Definir uma função de teste
def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    # Criando um cliente de teste com base na aplicação
    cliente = TestClient(app)
    # Pedir os recursos que estao na rota .../tarefas
    resposta = cliente.get("/tarefas")
    # Verificar se a expressao sao iguais
    assert resposta.status_code == status.HTTP_200_OK

# Verificar se o teste esta funcionando:
# python -m pytest

def test_quando_listar_tarefas_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    # O cabeçalho seja do tipo JSON
    assert resposta.headers["Content-Type"] == "application/json"

def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    # Instance = verifica se aquilo é uma lista. Pega a resposta.json e tranforma em formato lista
    assert isinstance(resposta.json(), list)

    def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    # Adicionando uma tarefa na lista
     TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    # Pega o 1ª elemento da lista
    assert "id" in resposta.json().pop()
    # Limpa a lista de tarefas. Sempre colocar para limpar
    TAREFAS.clear()

    # Colocar a aplicação no ar:
    # uvicorn --reload gerenciador_tarefas.gerenciador:app

