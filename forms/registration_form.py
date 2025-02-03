from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from model.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=50)])
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=6, message="Password must be at least 6 characters long."),
        EqualTo("confirm_password", message="Passwords must match.")
    ])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    # Custom validator to ensure the username is unique
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is already taken. Please choose a different one.")

    # Custom validator to ensure the email is unique
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is already registered. Please use a different one.")
