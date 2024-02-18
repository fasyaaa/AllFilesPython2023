# import tkinter as tk
import tkinter as tk

def hasil_prediksi():
    luaran_label.config(text="Hasil Prediksi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.pack()

# Membuat input nilai mata pelajaran
mata_pelajaran_labels = []
mata_pelajaran_entries = []
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i + 1}:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    mata_pelajaran_labels.append(label)
    mata_pelajaran_entries.append(entry)

# Membuat button Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack()

# Membuat label luaran hasil produksi
luaran_label = tk.Label(root, text="Hasil Prediksi: ", font=("Arial", 12))
luaran_label.pack()

# Menampilkan jendela GUI
root.geometry("400x400")
root.mainloop()
