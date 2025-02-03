from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, Length
from model.models import User


class PasswordResetRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Reset Password")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("No account found with that email.")


class PasswordResetForm(FlaskForm):
    password = PasswordField("New Password", validators=[
        DataRequired(),
        Length(min=6, message="Password must be at least 6 characters long."),
        EqualTo("confirm_password", message="Passwords must match.")
    ])
    confirm_password = PasswordField("Confirm New Password", validators=[DataRequired()])
    submit = SubmitField("Reset Password")