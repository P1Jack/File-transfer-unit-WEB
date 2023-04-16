from flask import Flask, url_for, request, render_template, send_from_directory, send_file, redirect
from uuid import uuid4
from first_page_form import FirstForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def generate_code():
    return str(uuid4())


@app.route('/main', methods=['GET'])
def main():
    return render_template('first_page.html', style=url_for('static', filename='css/style.css'))


@app.route('/give', methods=['GET'])
def give():
    code = generate_code()
    print(code)
    return render_template('give_page.html', style=url_for('static', filename='css/style.css'), cod=code)


@app.route('/download', methods=['GET', 'POST'])
def download():
    form = FirstForm()
    if form.validate_on_submit():
        return redirect('/main')
    return render_template('get_page.html', style=url_for('static', filename='css/style.css'), form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')