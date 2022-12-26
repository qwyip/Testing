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
    if re.match('Start',message):
        carousel_template_message = TemplateSendMessage(
            alt_text='免費教學影片',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/a/87EqciS',
                        title='成大資工必修課程',
                        text='60學分的必修有哪些QQ',
                        actions=[
                            MessageAction(
                                label='馬上查看有哪些課程',
                                text='大一\n微積分（一）、（二）\n程式設計（一）、（二） \n普通物理學（一）、（二） \n數位電路導論 \n綫性代數\n\n大二\n資料結構 \n演算法 \n機率與統計 \n數位系統導論 \n數位系統實驗 \n計算機組織 \n離散數學 \n電腦網路概論\n\n大三\n資訊專題（一）、（二） \n作業系統 \n編譯系統 \n微算機原理與應用（含實驗）'
                            ),
                            URIAction(
                                label='選課系統連接',
                                uri='https://course.ncku.edu.tw/index.php?c=qry11215&i=VGQAalZmVzwDd1ohBj1QMFE4CC0BOFJxVD8GalZsUmYGYAk9VWJWIVZqUmIFP1d5UT9TJgE7VWZXPFVmU24EewM7UDoANAdtUT8BM1FhAWpSegh8BW8FM1E7CC9QNFAwBCMPdwNQD2UFbA8sAjlWKVdgAmAAOwBwVDsCJQ9JAz5UIgByVmlXewNlWmgGNlAwUTIINAEwUmlUNgY5Vi1SJAZrCTZVY1ZwViNSKgV2V3lRZ1N3ATpVMlc8VXdTIQRuAzZQZQB2B3RRZQF6UWoBZ1I7CC0FNgVrUW0IYVA1UDIENg8hAzQPeAU5Dz8COFZ4VwwCdwA6AC9UbAI4DzkDNlQwAGtWM1c8Az1aaAZ8UHJROAg4AWtScVRgBmZWJlIjBg4Ja1U2VnBWa1IgBT9XaVFmUyYBRlUwVyRVblMpBH0DIVA6ADUHbFF8AXtRcgFrUmAINQVhBT5ReghkUGpQZQRoD2oDNQ87BTgPZwI4VmtXYQI8ADsAY1Q1AjIPMwNuVD8AYlZpV28DNlpjBjZQMVE5CGYBa1JgVD8GalZsUmYGYAkwVWJWL1YjUmkFNFdhUX5TYwEiVTxXZFVvU2QEOwMv'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/a1DBBLN',
                        title='110年成大資工系開設課程',
                        text='看看哪些課程所剩人數不多。。。',
                        actions=[
                            URIAction(
                                label='110年上學期',
                                uri='https://course-query.acad.ncku.edu.tw/index.php?c=qry11215&i=VTJRbAFnUj0HLlQlAmpRYA5nAnMCOQVzUjtUbgQ6BGUJYVA4WWxXI1VoVDUFO10tVmQJLghvUmRTbgQ1CTpZLFc4UWxSMARqATIAOFIyUmgELAcnAWlUNQ5mBndZLgghCjYOPw5yU3YAPFd0VWtSMwRvVHMNYFI0VGNVcgEzDXBVaVFlAWlSJQcmVDMCPVFzDmYCIgJqBWBSOlQlBDEEdglrUH1ZPldqVWFUPwVgXTVWNgk2CC9SdlNuBDYJOll1VzVRM1JwBCUBDABsUm9ScARsBycBaVQ1DmYGd1ljCH8KEg5nDidTdgA8V3pVOFI6BGRUYA1hUj5UMlVqAToNOVUoUSUBaVI0B29UdAIjUSgOLgJzAmsFIlI6VDIEOgR2CSVQblkzVzVVIFQmBTpdfFY9CTsIblInUzcEbglsWTtXNFExUmUEcwFoAHFSOlJjBG0HdgEFVCIOZwYoWTQIYgpiDm8ONVNvAGZXPVVgUjoELlQiDWtSMlRpVXIBbA1mVSNRIgEMUmkHOlR0AmtRIg5nAmMCagVzUkZUMAQiBG8JLVB9WSRXalVjVD4FI119ViUJNwg1Uj9TYQQ7CXtZPldrUWZSOwQ4AWkAMlI7UjsEbQdlAWhUaQ5mBmZZZggxCmkObA47Uz0APVc2VWFSMARuVDgNa1I2VGhVOQEyDTJVYlFmAWhSbgdvVGICa1E4DmcCYAJhBWRSO1R6BHMEbglhUDpZdVc3VXBUPwVjXTVWNwk3CCk='
                            ),
                            URIAction(
                                label='110年下學期',
                                uri='https://course-query.acad.ncku.edu.tw/index.php?c=qry11215&i=AWYGO1M1VzgCK1cmBm5SYwJrVCUGPVUjUzpVb1FvBmcOZgJqCD1UIAU4BGUHOVEhU2FVcl45VmBSbwQ1CzhbLgRrATwGZFQ6UmFVbVs7AzkHL1NzUjpUNQBoUyJXIFV8AT0PPlklUncGOll6AD4DYgFqBSILZgdhCD9Uc1poWSQBPQYyUztXIAIjVzAGOVJwAmpUdAZuVTBTO1UkUWcGdA5sAi8Ib1RpBTEEbwdiUTlTM1VqXnlWclJvBDYLOFt3BGYBYwYkVHVSX1U5W2YDIQdvU3NSOlQ1AGhTIldtVSIBGQ9mWXBSdwY6WXQAbQNrAWEFMQtnB2sIblRrWmFZbQF8BnJTO1cxAmpXdwYnUisCIlQlBm9VclM7VTNRbwZ0DiICPAhiVDYFcAR2BzhRcFM4VWdeOFYjUjYEbgtuWzkEZwFhBjFUI1I7VSRbMwMyB25TIlJWVCIAaVN9VzpVPwFpD25ZYlJuBmBZMwA1A2sBKwVzC20HZwg1VHNaN1kyAXcGdVNeV2wCP1d3Bm9SIQJrVDUGblUjU0dVMVF3Bm0OKgIvCHVUaQUzBG4HIVFxUyBVa15jVjtSYAQ7C3lbPAQ4ATYGb1RoUjpVZ1syA2oHblMxUjtUaQBoUzNXaFVsAWIPbVlsUjwGO1k4ADQDYQFrBWkLbQdjCDRUOFppWWYBNgYxUzpXawJqV2EGb1I7AmtUNgZlVTRTOlV7USYGbA5mAmgIJFQ0BSAEbwdhUTlTMlVrXn8='
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/o9R5qH6',
                        title='學生常用鏈接',
                        text='沒用過別説是成大生',
                        actions=[
                            URIAction(
                                label='資工系網',
                                uri='https://www.csie.ncku.edu.tw/zh-hant/ncku_csie/'
                            ),
                            URIAction(
                                label='全校獎學金查詢系統',
                                uri='http://sgd.adm.ncku.edu.tw/scholarship/'
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
