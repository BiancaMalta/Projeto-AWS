import boto3
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.utils import secure_filename
import os
import pymysql.cursors

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'ada'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'arquivos'
app.config['S3_BUCKET'] = 'projeto-ada-aws'  # Nome do bucket S3

# Função para verificar a extensão do arquivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Função para conectar ao banco de dados
def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Função para adicionar relatório ao banco de dados
def insert_report_to_database(filename, username):
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Report (filename, username) VALUES (%s, %s)", (filename, username))
            connection.commit()
    except Exception as e:
        print("Erro ao adicionar relatório ao banco de dados:", str(e))
    finally:
        if connection is not None:
            connection.close()

# Função para fazer upload de arquivo para o Amazon S3
def upload_to_s3(file_name, bucket_name):
    s3_client = boto3.client('s3', region_name='us-east-1')  # Define a região como us-east-1 (Norte da Virgínia)
    try:
        response = s3_client.upload_file(file_name, bucket_name, file_name)
    except Exception as e:
        print(e)
        return False
    return True

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
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_to_s3(os.path.join(app.config['UPLOAD_FOLDER'], filename), app.config['S3_BUCKET'])
            insert_report_to_database(filename, 'admin')
            return redirect(url_for('reports_page'))
        else:
            return 'Tipo de arquivo não permitido'
    return render_template('upload.html')

# Rota para exibir os relatórios enviados
@app.route('/reports')
def reports_page():
    # Recupera os relatórios do banco de dados
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Report")
            reports = cursor.fetchall()
            print("Relatórios recuperados do banco de dados:", reports)  # Imprime os relatórios recuperados
    finally:
        connection.close()
    
    # Passa os relatórios para o template HTML
    return render_template('reports.html', reports=reports)

# Rota para download de arquivos
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
