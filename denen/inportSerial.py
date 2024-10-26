import serial

# シリアルポートの設定 (ポート名とボーレートを適宜変更)
ser = serial.Serial('COM1', 9600,parity=serial.PARITY_EVEN)

while True:
    # シリアルデータを読み込む
    data = ser.readline()
    # デコードして文字列に変換 (必要に応じてエンコーディングを変更)
    decoded_data = data.decode('utf-8').rstrip()
    # コンソールに出力
    print(len(decoded_data))
    print(decoded_data)
    #TXを白に
    
