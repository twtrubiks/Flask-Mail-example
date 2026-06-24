# Flask-Mail-example
使用 Python Flask 完成寄信功能（已改用 [Flask-Mailman](https://flask-mailman.readthedocs.io/)）

* [Youtube Demo](https://youtu.be/qqOgDPSD3jc)

常看到別人的網站有寄信功能，今天教你使用 Python [Flask](https://flask.palletsprojects.com/) 快速建立一個。

> 📌 早期本範例使用 [Flask-Mail](https://github.com/pallets-eco/flask-mail) 實現，但該套件曾停更近 10 年（2014 ~ 2024），雖然 2024 年由 Pallets 社群生態接手（0.10.0），但維護量仍偏低。
> 因此本範例改用維護較積極的 [Flask-Mailman](https://flask-mailman.readthedocs.io/)（Django 風格 API 的替代方案，最新版 1.1.1）。

使用 Python [Flask](https://flask.palletsprojects.com/) 搭配 [Flask-Mailman](https://flask-mailman.readthedocs.io/) 實現寄信功能。

本篇使用 Gmail 當作範例，其他的信箱應該大同小異，請自行研究。

## 特色
* 搭配 [Flask-Mailman](https://flask-mailman.readthedocs.io/) 實現寄信功能。
* 前端使用 [Bootstrap 5](https://getbootstrap.com/)（透過 CDN 載入，免本地相依）。

## 安裝套件

```bash
pip install -r requirements.txt
```

`requirements.txt` 內容：

```
Flask>=3.1
Flask-Mailman>=1.1.1
```

記得將下方程式碼修改為自己的 Gmail 帳號和密碼
```python
from flask_mailman import Mail, EmailMessage

app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_DEFAULT_SENDER='admin <xxxxxx@gmail.com>',
    MAIL_USERNAME='xxxxxxx@gmail.com',
    MAIL_PASSWORD='xxxxxxxxx'
)

mail = Mail(app)
```

## 執行

```bash
python mail.py
```

預設會啟動在 http://127.0.0.1:5000 ，開啟首頁即可測試寄信。

更多 Flask-Mailman 用法，可參考 [Flask-Mailman 官方文件](https://flask-mailman.readthedocs.io/)



## 使用 Gmail 寄信 - 前置作業

### 第一步

可以參考官網的說明  [使用其他電子郵件程式讀取 Gmail 郵件 (透過 IMAP 協定)](https://support.google.com/mail/answer/7126229?hl=zh-Hant)

請先到自己的gmail，點右上角的齒輪，然後選 <b>設定</b>，

然後找到 <b>轉寄和POP/IMAP</b>，選擇 <b>啟用IMAP</b>，

記得按<b>儲存變更</b>。 這樣就完成第一步了。

![alt tag](http://i.imgur.com/lutH7Ox.jpg)

![alt tag](http://i.imgur.com/zu15YSB.jpg)

### 第二步

接著到 [Security Here](https://www.google.com/settings/security/lesssecureapps) 去開啟權限 (2022/5/30 後關閉)

![alt tag](http://i.imgur.com/nMWcYDh.jpg)

新的方法, [使用應用程式密碼登入帳戶](https://support.google.com/accounts/answer/185833?hl=zh-Hant)

到帳號的安全性, 一定要開啟兩步驟驗證,

![alt tag](https://i.imgur.com/IMSPInG.png)

接著設定應用程式密碼, 可以選 其他(自訂名稱)

![alt tag](https://i.imgur.com/ds2Ia36.png)

接著會跳出一組密碼

![alt tag](https://i.imgur.com/11qtT9M.png)

使用你的信箱帳號和這組應用程式密碼即可

![alt tag](https://i.imgur.com/tHavtEa.png)

## 執行畫面
首頁

![alt tag](http://i.imgur.com/QV7PSUF.jpg)

送出信件

![alt tag](http://i.imgur.com/nx3VKxR.jpg)

收到的信件內容

![alt tag](http://i.imgur.com/kM0uZMv.jpg)


P.S <br>

<b>可能遇到的問題一 :</b>

有時候你會遇到 <b>smtplib.SMTPAuthenticationError</b> 的錯誤訊息，

通常是你在 <b>使用 Gmail 寄信 - 前置作業</b> 的步驟二權限忘記開了。

<b>可能遇到的問題二 :</b>

你在本機 ( localhost )可以正常運作，但當你部署上去你自己的環境的時候，

卻又出現 <b>smtplib.SMTPAuthenticationError</b> 的錯誤訊息，

這時候你可以試著去改你的 Gmail 密碼，改成密碼是高強度並且第一個英文字母是大寫的!!

## 執行環境
* Python 3.13.13

## Reference
* [Flask-Mailman 官方文件](https://flask-mailman.readthedocs.io/)
* [Flask-Mailman GitHub](https://github.com/waynerv/flask-mailman)
* [Flask-Mail (pallets-eco)](https://github.com/pallets-eco/flask-mail)

## License
MIT license
