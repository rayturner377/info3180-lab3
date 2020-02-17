from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired 

class ContactForm(FlaskForm):
    name = StringField('Please enter your full name', validators=[DataRequired()])

    email = StringField('Please enter your e-mail address', validators=[DataRequired()])

    subject = StringField('Please enter the subject for your meassage', validators=[DataRequired()])

    message = TextAreaField('Please enter the message you would like to send.', validators=[DataRequired()])

    submit = SubmitField('Send')