from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect("nilai_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            kode_matakuliah TEXT,
            kelas TEXT,
            nilai REAL
        )
    """)
    conn.commit()
    conn.close()

def tambah_data(nama, kode_matakuliah, kelas, nilai):
    conn = sqlite3.connect("nilai_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO nilai (nama, kode_matakuliah, kelas, nilai)
        VALUES (?, ?, ?, ?)
    """, (nama, kode_matakuliah, kelas, nilai))
    conn.commit()
    conn.close()

def hapus_data(id):
    conn = sqlite3.connect("nilai_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM nilai WHERE id=?", (id,))
    conn.commit()
    conn.close()

def tampilkan_data():
    conn = sqlite3.connect("nilai_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nilai")
    data = cursor.fetchall()
    conn.close()

    return data

@app.route('/')
def index():
    create_table()
    data_nilai = tampilkan_data()
    return render_template('index.html', data_nilai=data_nilai)

@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    kode_matakuliah = request.form['kode_matakuliah']
    kelas = request.form['kelas']
    nilai = request.form['nilai']

    tambah_data(nama, kode_matakuliah, kelas, nilai)
    
    return redirect(url_for('index'))

@app.route('/hapus/<int:id>')
def hapus(id):
    hapus_data(id)
    return redirect(url_for('index'))

if __name__ == '_main_':
    app.run(debug=True)
