from flask import Flask, render_template, redirect, url_for, request
import datetime
from firebase_admin import firestore
from backend.db import db
from backend.config import configapp
# ===============================================

# Starter Template Flask
# By Makassar Coding

# ================================================
# Menentukan Nama Folder Penyimpanan Asset
app = Flask(__name__, static_folder='static', static_url_path='')
# Untuk Menggunakan flash pada flask
app.secret_key = 'iNiAdalahsecrEtKey'
# Untuk Mentukan Batas Waktu Session
app.permanent_session_lifetime = datetime.timedelta(days=7)
# Menentukan Jumlah Maksimal Upload File
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(configapp)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = {
            'created_at': firestore.SERVER_TIMESTAMP,
            'kehadiran': request.form['kehadiran'],
            'nama': request.form['nama'],
            'ucapan': request.form['ucapan'],
        }

        db.collection('ucapan').document().set(data, merge=True)

    docs = db.collection('ucapan').order_by('created_at', direction=firestore.Query.DESCENDING).limit(10).stream()
    ucapan = []
    for doc in docs:
        ucapan.append(doc.to_dict())
    return render_template('index.html', ucapan=ucapan)


# Untuk Menjalankan Program Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
