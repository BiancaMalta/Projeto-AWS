from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@hostname:port/database_name'
db = SQLAlchemy(app)

# Definição do modelo de relatório
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)

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
            add_report_to_database(filename, 'admin')  # Adiciona o relatório ao banco de dados
            return redirect(url_for('reports'))  # Redireciona para a página de relatórios
        else:
            return 'Tipo de arquivo não permitido'
    return render_template('upload.html')

# Função para adicionar relatório ao banco de dados
def add_report_to_database(filename, username):
    report = Report(filename=filename, username=username)
    db.session.add(report)
    db.session.commit()

# Rota para exibir os relatórios enviados
@app.route('/reports')
def reports():
    reports = Report.query.all()
    return render_template('reports.html', reports=reports)

# Rota para download de arquivos
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
