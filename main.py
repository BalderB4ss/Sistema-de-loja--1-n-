from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto

app = FastAPI(title="Gerenciamento Loja")

templates = Jinja2Templates(directory="templates")

@app.post("/categorias")
def criar_categoria(
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(nome=nome, descricao=descricao)
    db.add(nova_categoria)
    db.commit()

    return RedirectResponse(url="/categorias", status_code=303)