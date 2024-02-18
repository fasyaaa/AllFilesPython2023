import sqlite3
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambahkan data ke database
def tambah_data():
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_matematika = float(entry_matematika.get())
    nilai_kimia = float(entry_kimia.get())
    nilai_ekonomi = float(entry_ekonomi.get())
    nilai_seni = float(entry_seni.get())
    nilai_sejarah = float(entry_sejarah.get())
    nilai_geografi = float(entry_geografi.get())
    nilai_sains = float(entry_sains.get())
    nilai_pjok = float(entry_pjok.get())

    # Prediction for faculty
    nilai_list = [nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia, nilai_ekonomi, nilai_seni, nilai_sejarah, nilai_geografi, nilai_sains, nilai_pjok]
    prodi_list = ['Kedokteran', 'Teknik', 'Bahasa', 'Matematika', 'Kimia', 'Ekonomi', 'Seni', 'Sejarah', 'Geografi', 'Sains', 'Olahraga']
    prediksi = prodi_list[nilai_list.index(max(nilai_list))]

    hasil_prediksi.config(text=f"Prodi Pilihan: {prediksi}")

    # Saving data to the database
    conn = sqlite3.connect('percobaan2.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        Nama Siswa TEXT,
                        Biologi REAL,
                        Fisika REAL,
                        Inggris REAL,
                        Matematika REAL,
                        Kimia REAL,
                        Ekonomi REAL,
                        Seni REAL,
                        Sejarah REAL,
                        Geografi REAL,
                        Sains REAL,
                        PJOK REAL,
                        Prediksi Fakultas TEXT
                    )''')
    cursor.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nama, nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia, nilai_ekonomi, nilai_seni, nilai_sejarah, nilai_geografi, nilai_sains, prediksi))
    conn.commit()
    conn.close()

    entry_nama.delete(0, 'end')
    entry_biologi.delete(0, 'end')
    entry_fisika.delete(0, 'end')
    entry_inggris.delete(0, 'end')
    entry_matematika.delete(0, 'end')
    entry_kimia.delete(0, 'end')
    entry_ekonomi.delete(0, 'end')
    entry_seni.delete(0, 'end')
    entry_sejarah.delete(0, 'end')
    entry_geografi.delete(0, 'end')
    entry_sains.delete(0, 'end')
    entry_pjok.delete(0, 'end')

    messagebox.showinfo("Info", "Data telah disimpan dengan baik dan benar.")

# Creating GUI using Tkinter
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

label_matematika = tk.Label(root, text="Nilai Matematika:")
label_matematika.grid(row=4, column=0)
entry_matematika = tk.Entry(root)
entry_matematika.grid(row=4, column=1)

label_kimia = tk.Label(root, text="Nilai Kimia:")
label_kimia.grid(row=5, column=0)
entry_kimia = tk.Entry(root)
entry_kimia.grid(row=5, column=1)

label_ekonomi = tk.Label(root, text="Nilai Ekonomi:")
label_ekonomi.grid(row=6, column=0)
entry_ekonomi = tk.Entry(root)
entry_ekonomi.grid(row=6, column=1)

label_seni = tk.Label(root, text="Nilai Seni:")
label_seni.grid(row=7, column=0)
entry_seni = tk.Entry(root)
entry_seni.grid(row=7, column=1)

label_sejarah = tk.Label(root, text="Nilai Sejarah:")
label_sejarah.grid(row=8, column=0)
entry_sejarah = tk.Entry(root)
entry_sejarah.grid(row=8, column=1)

label_geografi = tk.Label(root, text="Nilai Geografi:")
label_geografi.grid(row=9, column=0)
entry_geografi = tk.Entry(root)
entry_geografi.grid(row=9, column=1)

label_sains = tk.Label(root, text="Nilai Sains:")
label_sains.grid(row=10, column=0)
entry_sains = tk.Entry(root)
entry_sains.grid(row=10, column=1)

label_pjok = tk.Label(root, text="Nilai Olahraga:")
label_pjok.grid(row=10, column=0)
entry_pjok = tk.Entry(root)
entry_pjok.grid(row=10, column=1)

button_submit = tk.Button(root, text="Submit", command=tambah_data)
button_submit.grid(row=11, column=0, columnspan=2)

hasil_prediksi = tk.Label(root, text="", font=("Times New Roman", 14))
hasil_prediksi.grid(row=12, column=0, columnspan=2)

root.mainloop()
