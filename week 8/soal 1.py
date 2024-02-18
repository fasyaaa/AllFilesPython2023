import sqlite3
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambahkan data ke database
def tambah_data():
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())

    # Menentukan prediksi fakultas
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi = 'Kedokteran'
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi = 'Teknik'
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi = 'Bahasa'
    else:
        prediksi = 'Tidak Dapat Diprediksi'
    
    hasil_prediksi.config(text=f"Prodi Pilihan : {prediksi} " )

    # Menyimpan data ke database
    conn = sqlite3.connect('percobaan1.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)",
                   (nama, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))
    conn.commit()
    conn.close()

    entry_nama.delete(0, 'end')
    entry_biologi.delete(0, 'end')
    entry_fisika.delete(0, 'end')
    entry_inggris.delete(0, 'end')

    messagebox.showinfo("info", "Data sudah tersimpan dengan baik dan benar ihiirrr !!")    
# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.grid(row=1, column=0)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1)

label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.grid(row=2, column=0)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1)

label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.grid(row=3, column=0)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1)

button_submit = tk.Button(root, text="Submit", command=tambah_data)
button_submit.grid(row=4, column=0, columnspan=2)

hasil_prediksi = tk.Label(root, text="", font=("Times New Roman", 14))
hasil_prediksi.grid(row=6, column=0, )


root.mainloop()
