from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import smtplib
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message/response')
def message():
    return render_template('message.html')

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get('email'),
    MAIL_PASSWORD = os.environ.get('password')
)
mail = Mail(app)

@app.route('/email/send', methods = ['GET', 'POST'])
def send():
    try:
        print(os.environ.get('password'))
        print(app.config.get('MAIL_PASSWORD'), app.config.get('MAIL_USERNAME'), "\n\n\n\n\n")
        result = request.form
        subject = str(result['subject'])
        email = str(result['email'])
        body = str(result['body'])

        msg = Message('Mail from your Website', sender=os.environ.get('email'), recipients=['tiegosullivanpsnl@gmail.com'] )
        msg.body = 'From: ' + email + 'Subject: ' + subject + "\n\n" + body
        msg.subject = subject
        mail.send(msg)
    except:
        return render_template('message.html', msg="Something went wrong")

    return render_template('message.html', msg="Message received, Thank you!")

if __name__ == "__main__":
    app.run(debug=True)