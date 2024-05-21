from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String)
  prompt = db.Column(db.String)
  saida = db.Column(db.String)

  def __init__(self, nome, prompt, saida,cep):
    self.nome = nome
    self.prompt = prompt
    self.saida = saida
    self.cep = cep