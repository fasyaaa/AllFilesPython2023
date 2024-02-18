from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect("kompetisi.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kompetisi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            asal_kampus TEXT,
            prodi TEXT,
            semester TEXT
        )
    """)
    conn.commit()
    conn.close()

def tambah_data(nama, asal_kampus, prodi, semester):
    conn = sqlite3.connect("kompetisi.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO kompetisi (nama, asal_kampus, prodi, semester)
        VALUES (?, ?, ?, ?)
    """, (nama, asal_kampus, prodi, semester))
    conn.commit()
    conn.close()

def hapus_data(id):
    conn = sqlite3.connect("kompetisi.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kompetisi WHERE id=?", (id,))
    conn.commit()
    conn.close()

def tampilkan_data():
    conn = sqlite3.connect("kompetisi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kompetisi")
    data = cursor.fetchall()
    conn.close()

    return data

@app.route('/')
def index():
    create_table()
    data_kompetisi = tampilkan_data()
    return render_template('index.html', data_kompetisi=data_kompetisi)

@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    asal_kampus = request.form['asal_kampus']
    prodi = request.form['prodi']
    semester = request.form['semester']

    tambah_data(nama, asal_kampus, prodi, semester)
    
    return redirect(url_for('index'))

@app.route('/hapus/<int:id>')
def hapus(id):
    hapus_data(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)