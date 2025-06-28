from flask import Flask, render_template, request, send_from_directory
import qrcode
import os

app = Flask(__name__)

# QR画像保存先
QR_PATH = os.path.join("static", "qr_code.png")

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_created = False
    if request.method == 'POST':
        data = request.form.get('text')
        if data:
            # QRコード生成と保存
            img = qrcode.make(data)
            img.save(QR_PATH)
            qr_created = True
    return render_template('index.html', qr_created=qr_created)

@app.route('/qr_code.png')
def qr_image():
    return send_from_directory('static', 'qr_code.png')

if __name__ == '__main__':
    app.run(debug=True)
