import sqlite3
import tkinter as tk
from tkinter import messagebox

def tambah_data():
    nama = entry_list[0].get()
    nilai_list = [float(entry.get()) for entry in entry_list[1:]]

    prodi_list = ['Kedokteran', 'Teknik', 'Bahasa', 'Matematika', 'Kimia', 'Ekonomi', 'Seni', 'Sejarah', 'Geografi', 'Nuklir']
    prediksi = prodi_list[nilai_list.index(max(nilai_list))]

    hasil_prediksi.config(text=f"Prodi Pilihan : {prediksi}")

    conn = sqlite3.connect('percobaan3.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS NilaiSiswa (
                   NamaSiswa TEXT,
                   Biologi REAL,
                   Fisika REAL,
                   Inggris REAL,
                   Matematika REAL,
                   Kimia REAL,
                   Ekonomi REAL,
                   Seni REAL,
                   Sejarah REAL,
                   Geografi REAL,
                   Nuklir REAL,
                   PrediksiFakultas TEXT
                )''')
    cursor.execute("INSERT INTO NilaiSiswa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (nama, *nilai_list, prediksi))
    conn.commit()
    conn.close()

    for entry in entry_list:
        entry.delete(0, 'end')

    messagebox.showinfo("Info", "Data telah disimpan dengan aman dan baik percayakan saja pada kami!!")

root = tk.Tk()
root.title("Input Nilai Siswa")

labels = ['Nama Siswa: ', 'Biologi: ', 'Fisika: ', 'Inggris: ', 'Matematika: ', 'Kimia: ', 'Ekonomi: ', 'Seni: ', 'Sejarah: ', 'Geografi: ', 'Nuklir: ']
entry_list = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entry_list.append(entry)

button_submit = tk.Button(root, text="Submit", command=tambah_data)
button_submit.grid(row=len(labels), column=0, columnspan=2)

hasil_prediksi = tk.Label(root, text="", font=("Times new roman", 14))
hasil_prediksi.grid(row=len(labels) + 1, column=0, columnspan=2)

root.mainloop()
