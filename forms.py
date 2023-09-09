from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Nombre:", validators=[DataRequired(message="Ingresa tu nombre")])
    password = PasswordField("Contraseña:", validators=[DataRequired(message="Ingresa tu password"), Length(min=4, max=16, message="La contraseña debe tener entre 4 y 16 caracteres")])
    submit = SubmitField("Enviar")
