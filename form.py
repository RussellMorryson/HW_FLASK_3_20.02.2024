from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class Registration(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Введите пароль повторно', validators=[DataRequired(), EqualTo('password')])