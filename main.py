from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Curso, Aluno

app = FastAPI(title="Gerenciamento Loja")

templates = Jinja2Templates(directory="templates")