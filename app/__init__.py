from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'f28c125e54e158'
app.config['MAIL_PASSWORD'] = 'a6724a139512b3'

mail = Mail(app)

from app import views