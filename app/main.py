from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import smtplib
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'dummy999email@gmail.com',
    MAIL_PASSWORD = 'idk'
)
mail = Mail(app)

@app.route('/email/send', methods = ['GET', 'POST'])
def send():
    return os.environ.get('password')
    result = request.form
    subject = str(result['subject'])
    email = str(result['email'])
    body = str(result['body'])

    msg = Message('Mail from your Website', sender='jamiejobobrien@gmail.com', recipients=['tiegosullivanpsnl@gmail.com'] )
    msg.body = 'From: ' + email + 'Subject: ' + subject + "\n\n" + body
    msg.subject = subject
    mail.send(msg)

    return '<h1>Message sent</h1>'

if __name__ == "__main__":
    app.run(debug=True)