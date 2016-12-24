from flask import *
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_DEFAULT_SENDER=('admin', 'xxxxxxxx@gmail.com'),
    MAIL_MAX_EMAILS=10,
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
    message = '這是 flask-mail example <br> <br>' \
              '附上一張圖片 <br> <br>' \
              '<b  style="color:#FF4E4E" >新垣結衣</b>'
    msg = Message(
        subject=subject,
        recipients=[email],
        html=message
    )
    # msg.body = '純文字'
    with app.open_resource("static/images/image.jpg") as fp:
        msg.attach("image.jpg", "image/jpg", fp.read())
    mail.send(msg)

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

    with mail.connect() as conn:
        for user in users:
            subject = 'hello, {}'.format(user['name'])

            message = '這是 flask-mail example <br> <br>' \
                      '附上一張圖片 <br> <br>' \
                      '<b  style="color:#FF4E4E" >新垣結衣</b>'
            msg = Message(subject=subject,
                          recipients=[user['email']],
                          html=message,
                          )
            # msg.body = '純文字'
            with app.open_resource("static/image.jpg") as fp:
                msg.attach("image.jpg", "image/jpg", fp.read())
            conn.send(msg)

    return "請到你的信箱收信~ ^0^"


if __name__ == '__main__':
    app.run()
