import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("入力エラー", "テキストを入力してください")
        return

    # QRコード作成
    qr = qrcode.make(data)
    qr.save("qr_code.png")

    # 表示
    img = Image.open("qr_code.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# ウィンドウ設定
root = tk.Tk()
root.title("QRコード作成アプリ")
root.geometry("300x350")

# 入力欄
tk.Label(root, text="QRコードにしたいテキスト：").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack()

# ボタン
tk.Button(root, text="QRコード生成", command=generate_qr).pack(pady=10)

# QRコード表示用ラベル
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
