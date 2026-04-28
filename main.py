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

@app.post("/produtos")
def criar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    estoque: int = Form(...),

    categoria_id: int = Form(...),
    db: Session = Depends(get_db)):

    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria == None:
        return "Erro!"
    else:

        novo_produto = Produto(nome=nome, preco=preco, estoque=estoque, categoria_id=categoria_id)
        db.add(novo_produto)
        db.commit()

        return RedirectResponse(url="/produtos", status_code=303)
    
@app.get("/listar_categoria")
def listar_categoria(
    request: Request,
    db: Session = Depends(get_db)
    ):

    categorias = db.query(Categoria).all()
    return templates.TemplateResponse(
        request,
        "categorias.html",
        {"request": request, "cursos": categorias}
    )