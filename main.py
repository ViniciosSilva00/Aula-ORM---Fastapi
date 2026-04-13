from fastapi import FastAPI

#python -m uvicorn main:app --reload

# Inicializar o app fastapi
app = FastAPI(title="Gestão Escolar")

# Metodos http: GET - POST - PUT - DELETE
@app.get("/")
def tela_inicial():
    return {"Mensagem": "Sistema Gestão Escolar"}

#Banco de dados
usuarios = {
     1: {"nome": "Gabriel", "idade": 33},
     2: {"nome": "Yasmin", "idade": 17},
     3: {"nome": "Kaua", "idade": 17},
}

@app.get("/alunos")
def listar_alunos():
    return {"usuarios":usuarios}