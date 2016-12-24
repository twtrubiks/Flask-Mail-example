# Flask-Mail-example
Flask-Mail - 使用 Python Flask 完成寄信功能

* [線上Demo mail 純文件](http://pythontt-twtrubikscode.rhcloud.com/mail_page)
* [線上Demo mail 圖片附件](http://pythontt-twtrubikscode.rhcloud.com/mail_page_img)
* [Youtube Demo](https://youtu.be/qqOgDPSD3jc)

常看到別人的網站有寄信功能，今天教你使用 Python [Flask](http://flask.pocoo.org/) 快速建立一個。

使用 Python [Flask](http://flask.pocoo.org/) 搭配 [Flask-Mail](http://pythonhosted.org/Flask-Mail/)  實現寄信功能。

本篇使用 Gmail 當作範例，其他的信箱應該大同小異，請自行研究。

## 特色
* 搭配 [Flask-Mail](http://pythonhosted.org/Flask-Mail/) 實現寄信功能。


## 安裝套件 Flask-Mail
請先確定電腦有安裝 [Python](https://www.python.org/)


### Flask-Mail
```
pip install Flask-Mail
```

記得將下方程式碼修改為自己的 Gmail 帳號和密碼
```
app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_DEFAULT_SENDER=('admin', 'xxxxxx@gmail.com'),
    MAIL_MAX_EMAILS=10,
    MAIL_USERNAME='xxxxxxx@gmail.com',
    MAIL_PASSWORD='xxxxxxxxx'
)

mail = Mail(app)
```

更多 Flask-Mail ，可參考  [Flask-Mail](http://pythonhosted.org/Flask-Mail/)



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

新的方法,

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
* Python 3.4.3

## Reference
* [Flask-Mail](http://pythonhosted.org/Flask-Mail/)

## License
MIT license
