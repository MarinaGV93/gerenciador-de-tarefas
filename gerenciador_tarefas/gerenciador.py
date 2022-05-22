# arquivo principal, onde iremos escrever o código da nossa aplicação

# Criando a aplicação
from curses.ascii import TAB

from fastapi import FastAPI

# Definir Tarefas
TAREFAS = []

app = FastAPI()

# Uma função para listar as tarefas
# Toda vez que chamar o verbo get em tarefas, irá executar esse codigo, por causa do @
@app.get("/tarefas")
def listar():
    # [] = uma lista de tarefas que esta vazia
    return TAREFAS
