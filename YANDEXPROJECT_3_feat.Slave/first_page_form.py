from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class FirstForm(FlaskForm):
    cod = StringField('Введите код для скачивания:', validators=[DataRequired()])
    download = SubmitField('Скачать')