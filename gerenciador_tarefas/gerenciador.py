# arquivo principal, onde iremos escrever o código da nossa aplicação

# Criando a aplicação
from enum import Enum
from uuid import UUID, uuid4

from fastapi import FastAPI, status
from pydantic import BaseModel, constr

# Definir Tarefas
TAREFAS = []

app = FastAPI()


class EstadosPossiveis(str, Enum):
    finalizado = "finalizado"
    nao_finalizado = "não finalizado"


class TarefaEntrada(BaseModel):
    titulo: constr(min_length=3, max_length=50)
    descricao: constr(max_length=140)
    estado: EstadosPossiveis = EstadosPossiveis.nao_finalizado


class Tarefa(TarefaEntrada):
    id: UUID


# Uma função para listar as tarefas
# Toda vez que chamar o verbo get em tarefas, 
# sirá executar esse codigo, por causa do @
@app.get("/tarefas")
def listar():
    # [] = uma lista de tarefas que esta vazia
    return TAREFAS


@app.post(
    "/tarefas", response_model=Tarefa, status_code=status.HTTP_201_CREATED
)
def criar(tarefa: TarefaEntrada):
    nova_tarefa = tarefa.dict()
    nova_tarefa.update({"id": uuid4()})
    TAREFAS.append(nova_tarefa)
    return nova_tarefa
