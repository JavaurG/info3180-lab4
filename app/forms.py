from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed,FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField("Login")

class UploadForm(FlaskForm):
     file = FileField('Image File', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

