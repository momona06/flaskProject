from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


def LoginForm(Form):
    username = StringField("Username", validators=[DataRequired(message="wrong name input!")])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField("Remember This")
    submit = SubmitField('Log in')

