from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Função para verificar a extensão do arquivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rota de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('upload_file'))
        else:
            return 'Login inválido'
    return render_template('login.html')

# Rota para fazer upload de arquivos
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Nenhum arquivo selecionado'
        file = request.files['file']
        if file.filename == '':
            return 'Nenhum arquivo selecionado'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'Arquivo {} enviado com sucesso'.format(filename)
        else:
            return 'Tipo de arquivo não permitido'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
