from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome_aluno = "Moisés"
    idade_aluno = 17
    
    usuario_dados = {"nome": "Ana", "email": "ana@email.com"}
    
    lista_alunos = [
        {"nome": "Carlos"},
        {"nome": "Beatriz"},
        {"nome": "Daniel"}
    ]
    
    nota_final = 8  
    return render_template('index.html', 
                           nome=nome_aluno, 
                           idade=idade_aluno,
                           usuario=usuario_dados,
                           alunos=lista_alunos,
                           nota=nota_final)

if __name__ == '__main__':
    app.run(debug=True)