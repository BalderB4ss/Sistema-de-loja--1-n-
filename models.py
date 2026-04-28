from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

    
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descicao = Column(String(200))

    produtos = relationship("Produto", back_populates="Categoria")
    
    def __repr__(self):
        return f"Produto: ID = {self.id} | Nome: {self.nome} | Descição: {self.descicao}"
    
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto: ID = {self.id} | Nome: {self.nome} | Preço: {self.preco:,.2f} | Em estoque: {self.estoque}"