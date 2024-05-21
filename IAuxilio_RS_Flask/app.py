from flask import Flask, render_template, request
from model import db, User
from gemini import Gemini_Connect
from cep import obter_info_cep

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'

db.init_app(app)

@app.route('/limpar_bd', methods=['POST'])
def limpar_banco_de_dados():
    with app.app_context():
        db.drop_all()
    return 'Banco de dados limpo com sucesso!'

@app.get('/')
def index_get():
  return render_template('index.html')

@app.post('/prompt')
def index_post():
  chat = Gemini_Connect() # Criando o chat, que faz conexão com a API do Gemini
  nome = request.form.get('nome')  # Entrada
  prompt = request.form.get('prompt') # Entrada
  cep = request.form.get('cep')
  info_cep = obter_info_cep(cep)
  if not cep:  # Verificar se o campo do CEP está vazio
      endereco = ""  # Definir o endereço como uma string vazia
  else:
      info_cep = obter_info_cep(cep)
      if info_cep:
          endereco = ", ".join(info_cep.values())
      else:
          return render_template('erro.html')
  response = chat.send_message(f'{prompt}{endereco} ') # Envio da mensagem para o Gemini
  saida = response.text.replace('*','') # Saída
  usuario = User(nome,prompt,saida,cep) # Criação de uma instância de User 
  db.session.add(usuario) # Adicionando o usuario criado no Banco SQLite 
  db.session.commit() # Confirma o comando 
  return render_template('saida.html', saida=saida)  # Exibe tela com a saída

if __name__ == '__main__':
  with app.app_context():
      db.create_all()
  app.run(debug=True)

