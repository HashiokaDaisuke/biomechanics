#

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import serial
import time

# Googleスプレッドシートの認証情報
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\dadas\Documents\jrk\wttk-denen-shahan-ec0a1e4c8737.json', scope)
client = gspread.authorize(creds)

# 開くスプレッドシートとシート名を指定
sheet = client.open('wttk-denen_test').worksheet('results')

# シリアルポートの設定
ser = serial.Serial('COM1', 9600,parity=serial.PARITY_EVEN)  # ポート名とボーレートを適宜変更

while True:
    # シリアルデータの読み込み
    data = ser.readline().decode('utf-8').rstrip()
    if len(data) > 0
       # Googleスプレッドシートに追記
        sheet.append_row([data, time.strftime(r"%Y-%m-%d %H:%M:%S")])
 
    # 一定時間待つ
    time.sleep(1)