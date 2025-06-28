from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# データ読み込み
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# データ保存
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '匿名')
        text = request.form.get('text', '')
        parent_id = request.form.get('parent_id', None)
        new_comment = {
            'id': datetime.now().timestamp(),
            'name': name,
            'text': text,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'parent_id': float(parent_id) if parent_id else None
        }
        data = load_data()
        data.append(new_comment)
        save_data(data)
        return redirect(url_for('index'))

    data = load_data()
    return render_template('index.html', comments=data)
    
if __name__ == '__main__':
    app.run(debug=True)
