from flask import *
from flask_mailman import Mail, EmailMessage

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_DEFAULT_SENDER='admin <xxxxxxxx@gmail.com>',
    MAIL_USERNAME='xxxxxxxx@gmail.com',
    MAIL_PASSWORD='xxxxxxxxxxx'
)

mail = Mail(app)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/send_mail", methods=['POST'])
def send_mail():
    email = request.form['email'].strip()
    subject = 'Hello'
    message = '這是 flask-mailman example <br> <br>' \
              '附上一張圖片 <br> <br>' \
              '<b  style="color:#FF4E4E" >新垣結衣</b>'
    msg = EmailMessage(
        subject=subject,
        body=message,
        to=[email]
    )
    msg.content_subtype = "html"
    with app.open_resource("static/images/image.jpg") as fp:
        msg.attach("image.jpg", fp.read(), "image/jpg")
    msg.send()

    # return "請到你的信箱收信~ ^0^"
    return render_template("thank.html")


@app.route("/Bulk_emails")
def Bulk_emails():
    """批次寄信"""
    users = [
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
    ]

    with mail.get_connection() as connection:
        for user in users:
            subject = 'hello, {}'.format(user['name'])

            message = '這是 flask-mailman example <br> <br>' \
                      '附上一張圖片 <br> <br>' \
                      '<b  style="color:#FF4E4E" >新垣結衣</b>'
            msg = EmailMessage(
                subject=subject,
                body=message,
                to=[user['email']],
                connection=connection
            )
            msg.content_subtype = "html"
            with app.open_resource("static/images/image.jpg") as fp:
                msg.attach("image.jpg", fp.read(), "image/jpg")
            msg.send()

    return "請到你的信箱收信~ ^0^"


if __name__ == '__main__':
    app.run()
