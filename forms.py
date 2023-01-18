from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, input_required

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    gr_no = IntegerField('gr_no', validators=[DataRequired()])
    branch = SelectField('branch', choices=[(1,'AIDS'),(2,'EXTC'),(3,'IT')], validators=[input_required()])
    email = StringField('email id', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password_conf = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me!')
    submit = SubmitField('login')
    