from flask import Flask, url_for, request, render_template, send_from_directory, send_file, redirect
from code_generator import get_code
from first_page_form import FirstForm
from werkzeug.utils import secure_filename
from data import db_session


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mkv', 'dat', 'py'}
db_session.global_init("db/blogs.db")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/main', methods=['GET'])
def main():
    return render_template('first_page.html', style=url_for('static', filename='css/style.css'))


@app.route('/give', methods=['GET', 'POST'])
def give():
    code = get_code()
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save('C:\\' + secure_filename(
                file.filename))
    return render_template('give_page.html', style=url_for('static', filename='css/style.css'), cod=code)


@app.route('/download', methods=['POST', 'GET'])
def download():
    form = FirstForm()
    if request.method == 'GET':
        return render_template('get_page.html', style=url_for('static', filename='css/style.css'), form=form)
    elif request.method == 'POST':
        return redirect('/downloaded')
        '''return send_file('C:\\Programs\\програмирование\\для себя\\yandex_transmiter\\ЦДЗ_3.3.png', as_attachment=True,
                         mimetype='png', download_name='test.png')'''


@app.route('/downloaded')
def downloaded():
    return render_template('downloaded_page.html', style=url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')