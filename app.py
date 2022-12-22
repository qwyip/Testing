# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
多樣版組合按鈕CarouselTemplate
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('sxZvkJ/GC7RdtY6jmav7xB9TFcmTIqZw9FJ5zF4rQMKUVwuZGl467dBL8bzvN/8Yor8geOWVqc06sa6ufPEVwipidocTrCgYCYRUoMf9RMGL3Z/dCCRwGnQ3e4TdRHpPua15cjRHUiYRz3evDJQXrgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1c2ab0310db47ca0710b64bbb976e3b0')

line_bot_api.push_message('U146570034b8d6111d1e048e2749cd88b', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('告訴我秘密',message):
        carousel_template_message = TemplateSendMessage(
            alt_text='免費教學影片',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='成大資工必修課程',
                        text='60學分的必修有哪些QQ',
                        actions=[
                            MessageAction(
                                label='大一課程',
                                text='微積分（一）、（二）\n 程式設計（一）、（二） \n 普通物理學（一）、（二） \n 數位電路導論 \n 綫性代數'
                            ),
                            MessageAction(
                                label='大二課程',
                                text='資料結構 \n 演算法 \n 機率與統計 \n 數位系統導論 \n 數位系統實驗 \n 計算機組織 \n 離散數學 \n 電腦網路概論'
                            ),
                            MessageAction(
                                label='大三課程',
                                text='資訊專題（一）、（二） \n 作業系統 \n 編譯系統 \n 微算機原理與應用（含實驗'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='Line Bot聊天機器人',
                        text='台灣最廣泛使用的通訊軟體',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='Line Bot申請與串接'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=2532'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='Telegram Bot聊天機器人',
                        text='唯有真正的方便，能帶來意想不到的價值',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='Telegrame申請與串接'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=2648'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
