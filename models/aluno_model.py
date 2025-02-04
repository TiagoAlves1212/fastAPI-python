from core.configs import settings
from sqlalchemy import Column, Integer, String, Float, Boolean

class AlunoModel(settings.DBBaseModel):
    __tablename__ = 'alunos'
    matricula = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    idade = Column(Integer, nullable=False)
    curso = Column(String(150))
    nota = Column(Float)
    aprovado = Column(Boolean, default=False)